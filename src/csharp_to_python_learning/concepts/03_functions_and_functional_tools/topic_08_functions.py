"""
# 8. Functions

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Functions are first-class objects in Python, so you can pass and return them directly. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
```

## Advanced Python example
```python
def pipeline(value: int, *steps):
    result = value
    for step in steps:
        result = step(result)
    return result

print(pipeline(5, lambda x: x + 1, lambda x: x * 3))
```

## Detailed explanation
Functions are first-class objects in Python, so you can pass and return them directly. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Functions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Functions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 5
- 18
"""

from __future__ import annotations


def simple_python_example() -> None:
    def add(a: int, b: int) -> int:
        return a + b

    print(add(2, 3))


def advanced_python_example() -> None:
    def pipeline(value: int, *steps):
        result = value
        for step in steps:
            result = step(result)
        return result

    print(pipeline(5, lambda x: x + 1, lambda x: x * 3))


def main() -> None:
    print("=== 8. Functions ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
