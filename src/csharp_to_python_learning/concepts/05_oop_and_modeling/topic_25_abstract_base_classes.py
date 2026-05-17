"""
# 25. Abstract base classes

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: ABCs define explicit contracts and can also provide reusable default behavior. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, key: str) -> str: ...

class InMemoryRepository(Repository):
    def get(self, key: str) -> str:
        return f"value:{key}"

print(InMemoryRepository().get("x"))
```

## Advanced Python example
```python
from collections.abc import Iterable

class CsvLike:
    def __iter__(self):
        yield from ["a,b", "c,d"]

print(isinstance(CsvLike(), Iterable))
```

## Detailed explanation
ABCs define explicit contracts and can also provide reusable default behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Abstract base classes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Abstract base classes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- value:x
- True
"""

from __future__ import annotations


def simple_python_example() -> None:
    from abc import ABC, abstractmethod

    class Repository(ABC):
        @abstractmethod
        def get(self, key: str) -> str: ...

    class InMemoryRepository(Repository):
        def get(self, key: str) -> str:
            return f"value:{key}"

    print(InMemoryRepository().get("x"))


def advanced_python_example() -> None:
    from collections.abc import Iterable

    class CsvLike:
        def __iter__(self):
            yield from ["a,b", "c,d"]

    print(isinstance(CsvLike(), Iterable))


def main() -> None:
    print("=== 25. Abstract base classes ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
