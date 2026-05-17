"""
# 44. Dependency management

## What C# developers usually expect
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Pin dependencies and commit lock files for deterministic builds across machines and CI. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
dependencies = ["httpx>=0.28", "pydantic>=2.8"]
print(len(dependencies))
```

## Advanced Python example
```python
groups = {"runtime": ["httpx"], "dev": ["pytest", "ruff", "mypy"]}
print(sorted(groups["dev"]))
```

## Detailed explanation
Pin dependencies and commit lock files for deterministic builds across machines and CI. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Dependency management` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Dependency management`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 2
- ['mypy', 'pytest', 'ruff']
"""

from __future__ import annotations


def simple_python_example() -> None:
    dependencies = ["httpx>=0.28", "pydantic>=2.8"]
    print(len(dependencies))


def advanced_python_example() -> None:
    groups = {"runtime": ["httpx"], "dev": ["pytest", "ruff", "mypy"]}
    print(sorted(groups["dev"]))


def main() -> None:
    print("=== 44. Dependency management ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
