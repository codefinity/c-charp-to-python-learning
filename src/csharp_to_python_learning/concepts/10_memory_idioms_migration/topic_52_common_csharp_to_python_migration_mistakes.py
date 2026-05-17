"""
# 52. Common C# to Python migration mistakes

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def append_bad(item, bucket=[]):  # noqa: B006 - intentional pitfall demo
    bucket.append(item)
    return bucket

print(append_bad(1), append_bad(2))
```

## Advanced Python example
```python
def append_good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket

print(append_good(1), append_good(2))
```

## Detailed explanation
Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Common C# to Python migration mistakes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Common C# to Python migration mistakes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- [1, 2]
- [1] [2]

## Further Study
Practice migrations by porting one real .NET utility at a time and measuring readability, testability, and performance.
"""

from __future__ import annotations


def simple_python_example() -> None:
    def append_bad(item, bucket=[]):  # noqa: B006 - intentional pitfall demo
        bucket.append(item)
        return bucket

    print(append_bad(1), append_bad(2))


def advanced_python_example() -> None:
    def append_good(item, bucket=None):
        bucket = [] if bucket is None else bucket
        bucket.append(item)
        return bucket

    print(append_good(1), append_good(2))


def main() -> None:
    print("=== 52. Common C# to Python migration mistakes ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
