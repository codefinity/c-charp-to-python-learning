"""
# 23. Enums

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
enum Status { Pending, Done }
Console.WriteLine(Status.Done);
```

Advanced equivalent:
```csharp
var env = "prod";
Console.WriteLine(env.ToUpperInvariant());
```

## Python equivalent
Python approaches this concept with less ceremony: Enums model closed sets of values and avoid stringly-typed logic in business rules. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    DONE = auto()

print(Status.DONE.name)
```

## Advanced Python example
```python
from enum import StrEnum

class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"

print(Environment.PROD.upper())
```

## Detailed explanation
Enums model closed sets of values and avoid stringly-typed logic in business rules. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Enums` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Enums`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- DONE
- PROD
"""

from __future__ import annotations


def simple_python_example() -> None:
    from enum import Enum, auto

    class Status(Enum):
        PENDING = auto()
        DONE = auto()

    print(Status.DONE.name)


def advanced_python_example() -> None:
    from enum import StrEnum

    class Environment(StrEnum):
        DEV = "dev"
        PROD = "prod"

    print(Environment.PROD.upper())


def main() -> None:
    print("=== 23. Enums ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
