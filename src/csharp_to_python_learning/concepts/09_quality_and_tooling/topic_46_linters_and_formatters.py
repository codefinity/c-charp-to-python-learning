"""
# 46. Linters and formatters

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
Console.WriteLine("use: uv run ruff check .");
Console.WriteLine("use: uv run ruff format .");
```

Advanced equivalent:
```csharp
var qualityGate = new Dictionary<string, string>
{
    ["lint"] = "ruff check",
    ["format"] = "ruff format",
    ["types"] = "mypy src",
};
Console.WriteLine(string.Join(" | ", qualityGate.Select(kv => $"{kv.Key}:{kv.Value}")));
```

## Python equivalent
Python approaches this concept with less ceremony: Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
snippet = "def add(a,b):\n return a+b\n"
print("use: uv run ruff check .")
print("use: uv run ruff format .")
```

## Advanced Python example
```python
quality_gate = {"lint": "ruff check", "format": "ruff format", "types": "mypy src"}
print(" | ".join(f"{k}:{v}" for k, v in quality_gate.items()))
```

## Detailed explanation
Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Linters and formatters` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Linters and formatters`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- use: uv run ruff check .
- lint:ruff check
"""

from __future__ import annotations


def simple_python_example() -> None:
    print("use: uv run ruff check .")
    print("use: uv run ruff format .")


def advanced_python_example() -> None:
    quality_gate = {"lint": "ruff check", "format": "ruff format", "types": "mypy src"}
    print(" | ".join(f"{k}:{v}" for k, v in quality_gate.items()))


def main() -> None:
    print("=== 46. Linters and formatters ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
