"""
# 11. Closures

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var count = 0;
int Inc() => ++count;
Console.WriteLine($"{Inc()} {Inc()}");
```

Advanced equivalent:
```csharp
var cache = new Dictionary<int, int>();
int Square(int value)
{
    if (!cache.ContainsKey(value)) cache[value] = value * value;
    return cache[value];
}
Console.WriteLine($"{Square(12)} {Square(12)}");
```

## Python equivalent
Python approaches this concept with less ceremony: Closures capture surrounding state, similar to C# captured variables in local functions/lambdas. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter = make_counter()
print(counter(), counter())
```

## Advanced Python example
```python
def memoized_square():
    cache: dict[int, int] = {}
    def run(value: int) -> int:
        if value not in cache:
            cache[value] = value * value
        return cache[value]
    return run

square = memoized_square()
print(square(12), square(12))
```

## Detailed explanation
Closures capture surrounding state, similar to C# captured variables in local functions/lambdas. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Closures` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Closures`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 1 2
- 144 144
"""

from __future__ import annotations


def simple_python_example() -> None:
    def make_counter():
        count = 0

        def inc():
            nonlocal count
            count += 1
            return count

        return inc

    counter = make_counter()
    print(counter(), counter())


def advanced_python_example() -> None:
    def memoized_square():
        cache: dict[int, int] = {}

        def run(value: int) -> int:
            if value not in cache:
                cache[value] = value * value
            return cache[value]

        return run

    square = memoized_square()
    print(square(12), square(12))


def main() -> None:
    print("=== 11. Closures ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
