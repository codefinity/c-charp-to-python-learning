"""
# 5. Collections: list, tuple, dict, set, frozenset

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
items = ["build", "test", "deploy"]
mapping = {"build": 1, "test": 2}
unique = set(items)
print(items[0], mapping["test"], "deploy" in unique)
```

## Advanced Python example
```python
permissions = frozenset({"read", "write"})
profile = ("nikhil", "senior", permissions)
print(profile[0], sorted(profile[2]))
```

## Detailed explanation
Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Collections: list, tuple, dict, set, frozenset` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Collections: list, tuple, dict, set, frozenset`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- build 2 True
- nikhil ['read', 'write']
"""

from __future__ import annotations


def simple_python_example() -> None:
    items = ["build", "test", "deploy"]
    mapping = {"build": 1, "test": 2}
    unique = set(items)
    print(items[0], mapping["test"], "deploy" in unique)


def advanced_python_example() -> None:
    permissions = frozenset({"read", "write"})
    profile = ("nikhil", "senior", permissions)
    print(profile[0], sorted(profile[2]))


def main() -> None:
    print("=== 5. Collections: list, tuple, dict, set, frozenset ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
