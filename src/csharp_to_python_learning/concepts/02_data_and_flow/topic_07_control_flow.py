"""
# 7. Control flow

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
for (var n = 0; n < 3; n++)
{
    if (n == 1) continue;
    Console.WriteLine($"value {n}");
}
```

Advanced equivalent:
```csharp
var target = 7;
var found = false;
foreach (var n in new[] { 1, 3, 5 })
{
    if (n == target)
    {
        Console.WriteLine("found");
        found = true;
        break;
    }
}
if (!found) Console.WriteLine("not found");
```

## Python equivalent
Python approaches this concept with less ceremony: Python control flow favors readability with indentation and expressive constructs like `for ... else`. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
for n in range(3):
    if n == 1:
        continue
    print("value", n)
```

## Advanced Python example
```python
target = 7
for n in [1, 3, 5]:
    if n == target:
        print("found")
        break
else:
    print("not found")
```

## Detailed explanation
Python control flow favors readability with indentation and expressive constructs like `for ... else`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Control flow` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Control flow`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- value 0
- not found
"""

from __future__ import annotations


def simple_python_example() -> None:
    for n in range(3):
        if n == 1:
            continue
        print("value", n)


def advanced_python_example() -> None:
    target = 7
    for n in [1, 3, 5]:
        if n == target:
            print("found")
            break
    else:
        print("not found")


def main() -> None:
    print("=== 7. Control flow ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
