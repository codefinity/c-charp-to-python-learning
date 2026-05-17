"""
# 21. Properties

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
class Temperature
{
    private double _celsius;
    public double Celsius
    {
        get => _celsius;
        set
        {
            if (value < -273.15) throw new ArgumentOutOfRangeException(nameof(value));
            _celsius = value;
        }
    }
}
var t = new Temperature { Celsius = 22.5 };
Console.WriteLine(t.Celsius);
```

Advanced equivalent:
```csharp
class Report
{
    private readonly List<int> _values;
    private int? _total;
    public Report(List<int> values) => _values = values;
    public int Total => _total ??= _values.Sum();
}
var r = new Report(new List<int> { 1, 2, 3 });
Console.WriteLine($"{r.Total} {r.Total}");
```

## Python equivalent
Python approaches this concept with less ceremony: Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
class Temperature:
    def __init__(self):
        self._celsius = 0.0

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

t = Temperature()
t.celsius = 22.5
print(t.celsius)
```

## Advanced Python example
```python
from functools import cached_property

class Report:
    def __init__(self, values: list[int]):
        self.values = values

    @cached_property
    def total(self) -> int:
        print("computing")
        return sum(self.values)

r = Report([1, 2, 3])
print(r.total, r.total)
```

## Detailed explanation
Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Properties` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Properties`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 22.5
- computing
"""

from __future__ import annotations


def simple_python_example() -> None:
    class Temperature:
        def __init__(self):
            self._celsius = 0.0

        @property
        def celsius(self) -> float:
            return self._celsius

        @celsius.setter
        def celsius(self, value: float) -> None:
            if value < -273.15:
                raise ValueError("below absolute zero")
            self._celsius = value

    t = Temperature()
    t.celsius = 22.5
    print(t.celsius)


def advanced_python_example() -> None:
    from functools import cached_property

    class Report:
        def __init__(self, values: list[int]):
            self.values = values

        @cached_property
        def total(self) -> int:
            print("computing")
            return sum(self.values)

    r = Report([1, 2, 3])
    print(r.total, r.total)


def main() -> None:
    print("=== 21. Properties ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
