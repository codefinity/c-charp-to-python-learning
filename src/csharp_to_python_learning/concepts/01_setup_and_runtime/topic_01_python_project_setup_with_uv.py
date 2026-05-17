"""
# 1. Python project setup with uv

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
commands = ["uv init", "uv sync", "uv run src/csharp_to_python_learning/concepts/.../topic_01_python_project_setup_with_uv.py"]
for command in commands:
    print(command)
```

## Advanced Python example
```python
tooling = {
    "dependencies": "uv add requests",
    "dev_dependencies": "uv add --dev pytest ruff mypy",
    "lock_refresh": "uv sync --upgrade",
}
print(", ".join(f"{k} => {v}" for k, v in tooling.items()))
```

## Detailed explanation
Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Python project setup with uv` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Python project setup with uv`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- uv init
- dependencies => uv add requests
"""

from __future__ import annotations


def simple_python_example() -> None:
    commands = [
        "uv init",
        "uv sync",
        "uv run src/csharp_to_python_learning/concepts/.../topic_01_python_project_setup_with_uv.py",
    ]
    for command in commands:
        print(command)


def advanced_python_example() -> None:
    tooling = {
        "dependencies": "uv add requests",
        "dev_dependencies": "uv add --dev pytest ruff mypy",
        "lock_refresh": "uv sync --upgrade",
    }
    print(", ".join(f"{k} => {v}" for k, v in tooling.items()))


def main() -> None:
    print("=== 1. Python project setup with uv ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
