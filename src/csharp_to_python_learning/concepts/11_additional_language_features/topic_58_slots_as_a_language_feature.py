"""
# 58. `__slots__` as a language feature

## What C# developers usually expect
C# developers usually expect object field layout to be explicit and stable.

## C# example
Simple equivalent:
```csharp
sealed class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
}
Console.WriteLine("has __dict__:False");
```

Advanced equivalent:
```csharp
record Event(int EventId, int Priority);
var e = new Event(101, 2);
Console.WriteLine($"slot dataclass:{e.Priority}");
```

## Python equivalent
`__slots__` restricts dynamic attribute creation and can reduce per-instance memory overhead.

## Simple Python example
```python
class Point:
    __slots__ = ("x", "y")
```

## Advanced Python example
```python
@dataclass(slots=True)
class Event:
    id: int
```

## Detailed explanation
Use slots in hot paths with many short-lived objects, but avoid them when dynamic attributes are required.

## Common mistakes for C# developers
1. Assuming slots make objects immutable.
2. Adding dynamic fields to slotted classes without planning.

## Exercises
1. Convert one high-volume model to slots and benchmark memory.
2. Decide where slots hurt flexibility in your codebase.

## Expected output
- has __dict__:False
- slot dataclass:2
"""

from __future__ import annotations

from dataclasses import dataclass


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


@dataclass(slots=True)
class Event:
    event_id: int
    priority: int


def simple_python_example() -> None:
    point = Point(2, 4)
    print(f"has __dict__:{hasattr(point, '__dict__')}")


def advanced_python_example() -> None:
    event = Event(event_id=101, priority=2)
    print(f"slot dataclass:{event.priority}")


def main() -> None:
    print("=== 58. `__slots__` as a language feature ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
