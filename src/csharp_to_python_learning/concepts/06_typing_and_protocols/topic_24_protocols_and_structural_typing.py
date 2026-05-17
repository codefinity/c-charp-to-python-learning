"""
# 24. Protocols and structural typing

## What C# developers usually expect
C# developers usually expect compile-time type contracts and explicit interfaces.

## C# example
Simple equivalent:
```csharp
interface IRunner { string Run(); }
class Job : IRunner { public string Run() => "ok"; }
string Execute(IRunner target) => target.Run();
Console.WriteLine(Execute(new Job()));
```

Advanced equivalent:
```csharp
interface ISerializer<in T> { string Serialize(T value); }
class IntSerializer : ISerializer<int> { public string Serialize(int value) => value.ToString(); }
Console.WriteLine(new IntSerializer().Serialize(42));
```

## Python equivalent
Python approaches this concept with less ceremony: Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from typing import Protocol

class Runner(Protocol):
    def run(self) -> str: ...

class Job:
    def run(self) -> str:
        return "ok"

def execute(target: Runner) -> str:
    return target.run()

print(execute(Job()))
```

## Advanced Python example
```python
from typing import Protocol, TypeVar

T = TypeVar("T")

class Serializer(Protocol[T]):
    def serialize(self, value: T) -> str: ...

class IntSerializer:
    def serialize(self, value: int) -> str:
        return str(value)

print(IntSerializer().serialize(42))
```

## Detailed explanation
Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Protocols and structural typing` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Protocols and structural typing`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- ok
- 42
"""

from __future__ import annotations


def simple_python_example() -> None:
    from typing import Protocol

    class Runner(Protocol):
        def run(self) -> str: ...

    class Job:
        def run(self) -> str:
            return "ok"

    def execute(target: Runner) -> str:
        return target.run()

    print(execute(Job()))


def advanced_python_example() -> None:
    from typing import Protocol, TypeVar

    T = TypeVar("T", contravariant=True)

    class Serializer(Protocol[T]):
        def serialize(self, value: T) -> str: ...

    class IntSerializer:
        def serialize(self, value: int) -> str:
            return str(value)

    print(IntSerializer().serialize(42))


def main() -> None:
    print("=== 24. Protocols and structural typing ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
