"""
# 29. Dunder methods and Python data model

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
class Team { public List<string> Members { get; } = new() { "a", "b", "c" }; }
Console.WriteLine(new Team().Members.Count);
```

Advanced equivalent:
```csharp
record Vector(int X, int Y)
{
    public static Vector operator +(Vector a, Vector b) => new(a.X + b.X, a.Y + b.Y);
}
Console.WriteLine(new Vector(1, 2) + new Vector(3, 4));
```

## Python equivalent
Python approaches this concept with less ceremony: Python objects participate in language syntax by implementing special (dunder) methods. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

print(len(Team(['a', 'b', 'c'])))
```

## Advanced Python example
```python
class Vector:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))
```

## Detailed explanation
Python objects participate in language syntax by implementing special (dunder) methods. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Dunder methods and Python data model` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Dunder methods and Python data model`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 3
- Vector(4, 6)
"""

from __future__ import annotations


def simple_python_example() -> None:
    class Team:
        def __init__(self, members):
            self.members = members

        def __len__(self):
            return len(self.members)

    print(len(Team(["a", "b", "c"])))


def advanced_python_example() -> None:
    class Vector:
        def __init__(self, x: int, y: int):
            self.x, self.y = x, y

        def __add__(self, other: Vector) -> Vector:
            return Vector(self.x + other.x, self.y + other.y)

        def __repr__(self) -> str:
            return f"Vector({self.x}, {self.y})"

    print(Vector(1, 2) + Vector(3, 4))


def main() -> None:
    print("=== 29. Dunder methods and Python data model ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
