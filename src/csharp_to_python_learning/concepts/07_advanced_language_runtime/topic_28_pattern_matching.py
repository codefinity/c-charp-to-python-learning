"""
# 28. Pattern matching

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def classify(value):
    match value:
        case 0:
            return "zero"
        case int() as n if n > 0:
            return "positive"
        case _:
            return "other"

print(classify(3))
```

## Advanced Python example
```python
from dataclasses import dataclass

@dataclass
class Event:
    kind: str
    size: int

def route(event: Event) -> str:
    match event:
        case Event(kind="upload", size=size) if size > 10:
            return "large-upload"
        case Event(kind="upload"):
            return "small-upload"
        case _:
            return "other"

print(route(Event("upload", 12)))
```

## Detailed explanation
Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Pattern matching` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Pattern matching`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- positive
- large-upload
"""

from __future__ import annotations


def simple_python_example() -> None:
    def classify(value):
        match value:
            case 0:
                return "zero"
            case int() as n if n > 0:
                return "positive"
            case _:
                return "other"

    print(classify(3))


def advanced_python_example() -> None:
    from dataclasses import dataclass

    @dataclass
    class Event:
        kind: str
        size: int

    def route(event: Event) -> str:
        match event:
            case Event(kind="upload", size=size) if size > 10:
                return "large-upload"
            case Event(kind="upload"):
                return "small-upload"
            case _:
                return "other"

    print(route(Event("upload", 12)))


def main() -> None:
    print("=== 28. Pattern matching ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
