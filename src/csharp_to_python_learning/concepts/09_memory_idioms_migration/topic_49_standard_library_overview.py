"""
# 49. Standard library overview

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import statistics
print(round(statistics.mean([10, 20, 40]), 2))
```

## Advanced Python example
```python
from itertools import pairwise
pairs = list(pairwise([1, 2, 3, 4]))
print(pairs[-1])
```

## Detailed explanation
The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Standard library overview` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Standard library overview`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 23.33
- (3, 4)
"""

from __future__ import annotations


def simple_python_example() -> None:
    import statistics

    print(round(statistics.mean([10, 20, 40]), 2))


def advanced_python_example() -> None:
    from itertools import pairwise

    pairs = list(pairwise([1, 2, 3, 4]))
    print(pairs[-1])


def main() -> None:
    print("=== 49. Standard library overview ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
