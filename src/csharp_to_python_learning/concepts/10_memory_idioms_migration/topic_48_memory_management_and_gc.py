"""
# 48. Memory management and garbage collection

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import gc
print(gc.isenabled())
```

## Advanced Python example
```python
import weakref

class Resource:
    pass

resource = Resource()
finalizer = weakref.finalize(resource, print, "resource finalized")
del resource
print(finalizer.alive in {True, False})
```

## Detailed explanation
CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Memory management and garbage collection` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Memory management and garbage collection`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- True
- True
"""

from __future__ import annotations


def simple_python_example() -> None:
    import gc

    print(gc.isenabled())


def advanced_python_example() -> None:
    import weakref

    class Resource:
        pass

    resource = Resource()
    finalizer = weakref.finalize(resource, print, "resource finalized")
    del resource
    print(finalizer.alive in {True, False})


def main() -> None:
    print("=== 48. Memory management and garbage collection ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
