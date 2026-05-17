"""
# 47. Performance and profiling

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import timeit
duration = timeit.timeit("sum(range(1000))", number=1000)
print(duration > 0)
```

## Advanced Python example
```python
import cProfile
import pstats
import io

profile = cProfile.Profile()
profile.enable()
sum(range(20_000))
profile.disable()
stream = io.StringIO()
pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(1)
print("function calls" in stream.getvalue())
```

## Detailed explanation
Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Performance and profiling` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Performance and profiling`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- True
- True
"""

from __future__ import annotations


def simple_python_example() -> None:
    import timeit

    duration = timeit.timeit("sum(range(1000))", number=1000)
    print(duration > 0)


def advanced_python_example() -> None:
    import cProfile
    import io
    import pstats

    profile = cProfile.Profile()
    profile.enable()
    sum(range(20_000))
    profile.disable()
    stream = io.StringIO()
    pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(1)
    print("function calls" in stream.getvalue())


def main() -> None:
    print("=== 47. Performance and profiling ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
