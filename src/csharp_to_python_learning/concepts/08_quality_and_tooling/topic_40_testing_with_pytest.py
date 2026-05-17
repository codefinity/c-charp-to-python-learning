"""
# 40. Testing with pytest

## What C# developers usually expect
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: `pytest` favors simple functions and powerful assertions for fast test feedback. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 2) == 4)
```

## Advanced Python example
```python
cases = [(2, 2, 4), (5, 7, 12)]
results = [left + right == expected for left, right, expected in cases]
print(all(results))
```

## Detailed explanation
`pytest` favors simple functions and powerful assertions for fast test feedback. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Testing with pytest` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Testing with pytest`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- True
- True
"""

from __future__ import annotations


def simple_python_example() -> None:
    def add(a: int, b: int) -> int:
        return a + b

    print(add(2, 2) == 4)


def advanced_python_example() -> None:
    cases = [(2, 2, 4), (5, 7, 12)]
    results = [left + right == expected for left, right, expected in cases]
    print(all(results))


def main() -> None:
    print("=== 40. Testing with pytest ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
