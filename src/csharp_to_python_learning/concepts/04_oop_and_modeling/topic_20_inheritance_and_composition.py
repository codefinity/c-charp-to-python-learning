"""
# 20. Inheritance and composition

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

print(Dog().speak())
```

## Advanced Python example
```python
class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"

class Notifier:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)

print(Notifier(EmailSender()).notify("deployed"))
```

## Detailed explanation
Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Inheritance and composition` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Inheritance and composition`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- woof
- email:deployed
"""

from __future__ import annotations


def simple_python_example() -> None:
    class Animal:
        def speak(self) -> str:
            return "..."

    class Dog(Animal):
        def speak(self) -> str:
            return "woof"

    print(Dog().speak())


def advanced_python_example() -> None:
    class EmailSender:
        def send(self, message: str) -> str:
            return f"email:{message}"

    class Notifier:
        def __init__(self, sender):
            self.sender = sender

        def notify(self, message: str) -> str:
            return self.sender.send(message)

    print(Notifier(EmailSender()).notify("deployed"))


def main() -> None:
    print("=== 20. Inheritance and composition ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
