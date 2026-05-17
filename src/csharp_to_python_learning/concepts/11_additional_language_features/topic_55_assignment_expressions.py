"""
# 55. Assignment expressions (`:=`)

## What C# developers usually expect
C# developers usually declare a variable before condition checks.

## C# example
```csharp
var size = items.Count;
if (size > 2) { Console.WriteLine(size); }
```

## Python equivalent
Python's walrus operator (`:=`) allows assignment inside expressions when it improves clarity.

## Simple Python example
```python
if (size := len(items)) > 2:
    print(size)
```

## Advanced Python example
```python
matches = [clean for item in raw if (clean := item.strip())]
```

## Detailed explanation
Use this feature sparingly for readable pipelines, loop conditions, and lightweight parsing.

## Common mistakes for C# developers
1. Overusing walrus in dense expressions.
2. Hiding important state changes inside nested conditions.

## Exercises
1. Refactor one parsing loop to use a single walrus assignment.
2. Compare readability with and without walrus in a code review.

## Expected output
- size:4
- ['A', 'B', 'C']
"""

from __future__ import annotations


def simple_python_example() -> None:
    items = ["a", "b", "c", "d"]
    if (size := len(items)) > 2:
        print(f"size:{size}")


def advanced_python_example() -> None:
    raw = [" A ", " ", "B", "", " C"]
    cleaned = [item for raw_item in raw if (item := raw_item.strip())]
    print(cleaned)


def main() -> None:
    print("=== 55. Assignment expressions (`:=`) ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
