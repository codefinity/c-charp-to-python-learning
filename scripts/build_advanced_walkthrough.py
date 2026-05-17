from __future__ import annotations

import ast
import re
from pathlib import Path
from textwrap import dedent

README_PATH = Path("README.md")
CONCEPTS_ROOT = Path("src/csharp_to_python_learning/concepts")
START_MARKER = "<!-- ADVANCED_WALKTHROUGH_START -->"
END_MARKER = "<!-- ADVANCED_WALKTHROUGH_END -->"
TOC_ENTRY = "- [Advanced Walkthrough for C# Developers](#advanced-walkthrough-for-c-developers)"


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


def extract_advanced_code(source_text: str, module: ast.Module) -> str:
    lines = source_text.splitlines()
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == "advanced_python_example":
            if not node.body:
                return "pass"
            start = node.body[0].lineno
            end = node.body[-1].end_lineno
            if end is None:
                end = node.body[-1].lineno
            snippet = "\n".join(lines[start - 1 : end])
            return dedent(snippet).strip()
    return "pass"


def concept_block(path: Path) -> str:
    source_text = path.read_text(encoding="utf-8")
    module = ast.parse(source_text)
    docstring_text = ast.get_docstring(module, clean=False) or ""
    title, sections = parse_sections(docstring_text)
    advanced_code = extract_advanced_code(source_text, module)
    rel = path.as_posix()
    number = topic_number(path)

    return (
        f"### {number}. {title}\n"
        f"Source: [{rel}]({rel})\n\n"
        "**What C# developers usually expect**\n"
        f"{sections.get('What C# developers usually expect', 'See source file docstring.')}\n\n"
        "**C# example**\n"
        f"{sections.get('C# example', 'See source file docstring.')}\n\n"
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


def build_section() -> str:
    concept_files = sorted(CONCEPTS_ROOT.rglob("topic_*.py"), key=topic_number)
    blocks = [concept_block(path) for path in concept_files]
    intro = (
        "## Advanced Walkthrough for C# Developers\n"
        "This section pulls advanced examples directly from each concept file and explains how to map them from familiar C#/.NET patterns to Python production practices.\n"
        "Use this as the deep-dive track after you run each concept script once.\n\n"
    )
    return f"{START_MARKER}\n{intro}{'\n\n'.join(blocks)}\n{END_MARKER}"


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


def ensure_toc_entry(readme: str) -> str:
    if TOC_ENTRY in readme:
        return readme

    anchor = "- [Tutorial Concepts](#tutorial-concepts)\n"
    if anchor in readme:
        return readme.replace(anchor, anchor + TOC_ENTRY + "\n", 1)

    return readme


def main() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    readme = ensure_toc_entry(readme)
    walkthrough = build_section()
    readme = insert_or_replace_walkthrough(readme, walkthrough)
    README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
