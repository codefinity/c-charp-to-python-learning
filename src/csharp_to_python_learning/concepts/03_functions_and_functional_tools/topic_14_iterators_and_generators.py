"""
# 14. Iterators and generators

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def count_up(limit: int):
    current = 0
    while current < limit:
        yield current
        current += 1

print(list(count_up(4)))
```

## Advanced Python example
```python
def lines():
    yield "alpha"
    yield "beta"

def upper(values):
    for value in values:
        yield value.upper()

print(list(upper(lines())))
```

## Detailed explanation
Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Iterators and generators` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Iterators and generators`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- [0, 1, 2, 3]
- ['ALPHA', 'BETA']
"""

from __future__ import annotations


def simple_python_example() -> None:
    def count_up(limit: int):
        current = 0
        while current < limit:
            yield current
            current += 1

    print(list(count_up(4)))


def advanced_python_example() -> None:
    def lines():
        yield "alpha"
        yield "beta"

    def upper(values):
        for value in values:
            yield value.upper()

    print(list(upper(lines())))


def main() -> None:
    print("=== 14. Iterators and generators ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
