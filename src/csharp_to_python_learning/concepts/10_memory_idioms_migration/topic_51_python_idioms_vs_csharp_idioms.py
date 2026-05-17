"""
# 51. Python idioms versus C# idioms

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Translate intent, not syntax: many C# patterns have shorter Pythonic forms. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
numbers = [1, 2, 3, 4]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

## Advanced Python example
```python
records = [{"name": "a", "score": 10}, {"name": "b", "score": 7}]
best = max(records, key=lambda r: r["score"])
print(best["name"])
```

## Detailed explanation
Translate intent, not syntax: many C# patterns have shorter Pythonic forms. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Python idioms versus C# idioms` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Python idioms versus C# idioms`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- [2, 4]
- a
"""

from __future__ import annotations


def simple_python_example() -> None:
    numbers = [1, 2, 3, 4]
    evens = [n for n in numbers if n % 2 == 0]
    print(evens)


def advanced_python_example() -> None:
    from typing import TypedDict

    class ScoreRecord(TypedDict):
        name: str
        score: int

    records: list[ScoreRecord] = [{"name": "a", "score": 10}, {"name": "b", "score": 7}]
    best = max(records, key=lambda r: r["score"])
    print(best["name"])


def main() -> None:
    print("=== 51. Python idioms versus C# idioms ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
