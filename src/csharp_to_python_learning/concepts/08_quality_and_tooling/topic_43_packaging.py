"""
# 43. Packaging

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Packaging turns source code into installable artifacts with metadata and entry points. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
metadata = {
    "name": "csharp-to-python-learning",
    "entry_point": "python -m csharp_to_python_learning",
}
print(metadata["name"])
```

## Advanced Python example
```python
build_steps = ["uv sync", "uv run -m pytest", "uv build"]
print(" -> ".join(build_steps))
```

## Detailed explanation
Packaging turns source code into installable artifacts with metadata and entry points. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Packaging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Packaging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- csharp-to-python-learning
- uv sync -> uv run -m pytest -> uv build
"""

from __future__ import annotations


def simple_python_example() -> None:
    metadata = {
        "name": "csharp-to-python-learning",
        "entry_point": "python -m csharp_to_python_learning",
    }
    print(metadata["name"])


def advanced_python_example() -> None:
    build_steps = ["uv sync", "uv run -m pytest", "uv build"]
    print(" -> ".join(build_steps))


def main() -> None:
    print("=== 43. Packaging ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
