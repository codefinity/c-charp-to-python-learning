"""
# 6. Slicing and unpacking

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var numbers = new List<int> { 10, 20, 30, 40, 50 };
var head = numbers[0];
var middle = numbers.Skip(1).Take(numbers.Count - 2).ToList();
var tail = numbers[^1];
Console.WriteLine($"{head} [{string.Join(", ", middle)}] {tail}");
```

Advanced equivalent:
```csharp
var window = Enumerable.Range(0, 100)
    .Select(n => n * n)
    .Skip(5)
    .Take(5)
    .ToList();
Console.WriteLine($"[{string.Join(", ", window)}]");
```

## Python equivalent
Python approaches this concept with less ceremony: Python slicing and unpacking replace many verbose loop/indexing patterns common in C#. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
numbers = [10, 20, 30, 40, 50]
head, *middle, tail = numbers
print(head, middle, tail)
```

## Advanced Python example
```python
from itertools import islice
stream = (n * n for n in range(100))
window = list(islice(stream, 5, 10))
print(window)
```

## Detailed explanation
Python slicing and unpacking replace many verbose loop/indexing patterns common in C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Slicing and unpacking` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Slicing and unpacking`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 10 [20, 30, 40] 50
- [25, 36, 49, 64, 81]
"""

from __future__ import annotations


def simple_python_example() -> None:
    numbers = [10, 20, 30, 40, 50]
    head, *middle, tail = numbers
    print(head, middle, tail)


def advanced_python_example() -> None:
    from itertools import islice

    stream = (n * n for n in range(100))
    window = list(islice(stream, 5, 10))
    print(window)


def main() -> None:
    print("=== 6. Slicing and unpacking ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
