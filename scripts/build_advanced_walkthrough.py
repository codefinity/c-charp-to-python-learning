from __future__ import annotations

import ast
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

README_PATH = Path("README.md")
CONCEPTS_ROOT = Path("src/csharp_to_python_learning/concepts")
PAGES_ROOT = Path("pages/advanced_walkthrough")

START_MARKER = "<!-- ADVANCED_WALKTHROUGH_START -->"
END_MARKER = "<!-- ADVANCED_WALKTHROUGH_END -->"
TOC_ENTRY = "- [Advanced Walkthrough for C# Developers](pages/advanced_walkthrough/README.md)"
ADVANCED_TOC_START = "<!-- ADVANCED_WALKTHROUGH_TOPICS_START -->"
ADVANCED_TOC_END = "<!-- ADVANCED_WALKTHROUGH_TOPICS_END -->"


@dataclass(frozen=True)
class ConceptEntry:
    number: int
    title: str
    block: str
    group: str
    page_name: str

    @property
    def page_rel(self) -> str:
        return Path("pages", "advanced_walkthrough", self.group, self.page_name).as_posix()

    @property
    def page_rel_from_pages_index(self) -> str:
        return Path(self.group, self.page_name).as_posix()


def topic_number(path: Path) -> int:
    match = re.search(r"topic_(\d+)_", path.name)
    if not match:
        raise ValueError(f"Could not read topic number from {path}")
    return int(match.group(1))


def parse_sections(docstring_text: str) -> tuple[str, dict[str, str]]:
    lines = docstring_text.strip().splitlines()
    title = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped.removeprefix("# ").strip()
            title = re.sub(r"^\d+\.\s*", "", title).strip()
            break

    matches = list(re.finditer(r"^## (?P<name>.+)$", docstring_text, flags=re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        section_name = match.group("name").strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(docstring_text)
        content = docstring_text[start:end].strip()
        sections[section_name] = content

    return title, sections


def extract_function_code(source_text: str, module: ast.Module, function_name: str) -> str:
    lines = source_text.splitlines()
    for node in module.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name:
            if not node.body:
                return "pass"
            start = node.body[0].lineno
            end = node.body[-1].end_lineno
            if end is None:
                end = node.body[-1].lineno
            snippet = "\n".join(lines[start - 1 : end])
            return dedent(snippet).strip()
    return "pass"


def concept_block(path: Path) -> tuple[str, int, str]:
    source_text = path.read_text(encoding="utf-8")
    module = ast.parse(source_text)
    docstring_text = ast.get_docstring(module, clean=False) or ""
    title, sections = parse_sections(docstring_text)
    simple_code = extract_function_code(source_text, module, "simple_python_example")
    advanced_code = extract_function_code(source_text, module, "advanced_python_example")
    rel = path.as_posix()
    number = topic_number(path)

    block = (
        f"### {number}. {title}\n"
        f"Source: [{rel}]({rel})\n\n"
        "**What C# developers usually expect**\n"
        f"{sections.get('What C# developers usually expect', 'See source file docstring.')}\n\n"
        "**C# example**\n"
        f"{sections.get('C# example', 'See source file docstring.')}\n\n"
        "**Simple Python example from this file**\n"
        "```python\n"
        f"{simple_code}\n"
        "```\n\n"
        "**Advanced Python example from this file**\n"
        "```python\n"
        f"{advanced_code}\n"
        "```\n\n"
        "**Python equivalent**\n"
        f"{sections.get('Python equivalent', 'See source file docstring.')}\n\n"
        "**Detailed explanation for C# developers**\n"
        f"{sections.get('Detailed explanation', 'See source file docstring.')}\n\n"
        "**Common mistakes for C# developers**\n"
        f"{sections.get('Common mistakes for C# developers', 'See source file docstring.')}\n\n"
        "**Exercises**\n"
        f"{sections.get('Exercises', 'See source file docstring.')}\n\n"
        "**Expected output**\n"
        f"{sections.get('Expected output', 'See source file docstring.')}\n"
    )
    return block, number, title


def slugify_filename(text: str) -> str:
    slug = text.strip().lower()
    slug = slug.replace("`", "")
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")


def discover_concept_files() -> list[Path]:
    discovered = sorted(CONCEPTS_ROOT.rglob("topic_*.py"))
    selected_by_topic: dict[int, Path] = {}
    for path in discovered:
        number = topic_number(path)
        current = selected_by_topic.get(number)
        if current is None or len(path.name) > len(current.name):
            selected_by_topic[number] = path
    return sorted(selected_by_topic.values(), key=topic_number)


def build_concept_entries(concept_files: list[Path]) -> list[ConceptEntry]:
    entries: list[ConceptEntry] = []
    for path in concept_files:
        block, number, title = concept_block(path)
        entries.append(
            ConceptEntry(
                number=number,
                title=title,
                block=block,
                group=path.parent.name,
                page_name=f"{number:02d}_{slugify_filename(title)}.md",
            )
        )
    return entries


def build_readme_walkthrough_section() -> str:
    content = (
        "## Advanced Walkthrough for C# Developers\n"
        "The full concept-by-concept walkthrough is available in the pages folder:\n"
        "- [Advanced Walkthrough Index](pages/advanced_walkthrough/README.md)\n"
    )
    return f"{START_MARKER}\n{content}\n{END_MARKER}"


def insert_or_replace_walkthrough(readme: str, walkthrough: str) -> str:
    if START_MARKER in readme and END_MARKER in readme:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(lambda _match: walkthrough, readme)

    needle = "## Python-Only Features"
    if needle in readme:
        return readme.replace(needle, f"{walkthrough}\n\n{needle}", 1)

    return readme + "\n\n" + walkthrough + "\n"


def build_advanced_toc_section(entries: list[ConceptEntry]) -> str:
    lines = [ADVANCED_TOC_START, TOC_ENTRY]
    for entry in entries:
        lines.append(f"  - [{entry.number}. {entry.title}]({entry.page_rel})")
    lines.append(ADVANCED_TOC_END)
    return "\n".join(lines)


def ensure_toc_entries(readme: str, entries: list[ConceptEntry]) -> str:
    toc_section = build_advanced_toc_section(entries)

    if ADVANCED_TOC_START in readme and ADVANCED_TOC_END in readme:
        pattern = re.compile(
            re.escape(ADVANCED_TOC_START) + r".*?" + re.escape(ADVANCED_TOC_END),
            flags=re.DOTALL,
        )
        return pattern.sub(lambda _match: toc_section, readme, count=1)

    if TOC_ENTRY in readme:
        return readme.replace(TOC_ENTRY, toc_section, 1)

    anchor = "- [Tutorial Concepts](#tutorial-concepts)\n"
    if anchor in readme:
        return readme.replace(anchor, anchor + toc_section + "\n", 1)

    return readme


def write_concept_pages(entries: list[ConceptEntry]) -> None:
    shutil.rmtree(PAGES_ROOT, ignore_errors=True)
    PAGES_ROOT.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, list[ConceptEntry]] = {}
    for entry in entries:
        target_dir = PAGES_ROOT / entry.group
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / entry.page_name).write_text(entry.block.rstrip() + "\n", encoding="utf-8")
        grouped.setdefault(entry.group, []).append(entry)

    index_lines = [
        "# Advanced Walkthrough Pages",
        "",
        "Exact topic text copied from README Advanced Walkthrough, grouped by concept folder.",
        "",
        "- [Back to main README](../../README.md)",
        "",
    ]
    for group in sorted(grouped):
        index_lines.append(f"## {group}")
        for entry in sorted(grouped[group], key=lambda value: value.number):
            index_lines.append(
                f"- [{entry.number}. {entry.title}]({entry.page_rel_from_pages_index})"
            )
        index_lines.append("")

    (PAGES_ROOT / "README.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
    )


def main() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    entries = build_concept_entries(discover_concept_files())
    readme = ensure_toc_entries(readme, entries)
    readme = insert_or_replace_walkthrough(readme, build_readme_walkthrough_section())
    README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
    write_concept_pages(entries)


if __name__ == "__main__":
    main()
