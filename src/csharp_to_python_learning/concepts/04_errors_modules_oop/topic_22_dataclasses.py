"""
# 22. Dataclasses

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Dataclasses are concise record-like types with optional immutability, ordering, and slots. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

print(User(1, "Nikhil"))
```

## Advanced Python example
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True, slots=True)
class Job:
    priority: int
    name: str
    tags: tuple[str, ...] = field(default_factory=tuple)

print(sorted([Job(2, "test"), Job(1, "build")])[0].name)
```

## Detailed explanation
Dataclasses are concise record-like types with optional immutability, ordering, and slots. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Dataclasses` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Dataclasses`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- User(id=1, name='Nikhil')
- build
"""

from __future__ import annotations


def simple_python_example() -> None:
    from dataclasses import dataclass

    @dataclass
    class User:
        id: int
        name: str

    print(User(1, "Nikhil"))


def advanced_python_example() -> None:
    from dataclasses import dataclass, field

    @dataclass(frozen=True, order=True, slots=True)
    class Job:
        priority: int
        name: str
        tags: tuple[str, ...] = field(default_factory=tuple)

    print(sorted([Job(2, "test"), Job(1, "build")])[0].name)


def main() -> None:
    print("=== 22. Dataclasses ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
