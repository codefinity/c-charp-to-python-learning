"""
# 19. Object-oriented programming

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
class Account:
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

a = Account("Nikhil")
a.deposit(50)
print(a.owner, a.balance)
```

## Advanced Python example
```python
from dataclasses import dataclass

@dataclass
class TaxedAmount:
    net: float
    tax_rate: float

    @property
    def gross(self) -> float:
        return self.net * (1 + self.tax_rate)

print(round(TaxedAmount(100, 0.18).gross, 2))
```

## Detailed explanation
Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Object-oriented programming` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Object-oriented programming`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- Nikhil 50
- 118.0
"""

from __future__ import annotations


def simple_python_example() -> None:
    class Account:
        def __init__(self, owner: str):
            self.owner = owner
            self.balance = 0

        def deposit(self, amount: int) -> None:
            self.balance += amount

    a = Account("Nikhil")
    a.deposit(50)
    print(a.owner, a.balance)


def advanced_python_example() -> None:
    from dataclasses import dataclass

    @dataclass
    class TaxedAmount:
        net: float
        tax_rate: float

        @property
        def gross(self) -> float:
            return self.net * (1 + self.tax_rate)

    print(round(TaxedAmount(100, 0.18).gross, 2))


def main() -> None:
    print("=== 19. Object-oriented programming ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
