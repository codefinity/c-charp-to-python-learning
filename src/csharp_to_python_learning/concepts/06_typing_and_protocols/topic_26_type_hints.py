"""
# 26. Type hints

## What C# developers usually expect
C# developers usually expect compile-time type contracts and explicit interfaces.

## C# example
Simple equivalent:
```csharp
static List<string> Normalize(List<string> names) =>
    names.Select(n => n.Trim()).Select(n => char.ToUpperInvariant(n[0]) + n[1..].ToLowerInvariant()).ToList();
Console.WriteLine($"[{string.Join(", ", Normalize(new List<string> { "  nikhil", "PRIYA " }))}]");
```

Advanced equivalent:
```csharp
var config = new Dictionary<string, object> { ["retries"] = 3, ["timeout"] = 1.5 };
Console.WriteLine(config["retries"]);
```

## Python equivalent
Python approaches this concept with less ceremony: Type hints improve readability and tooling without changing runtime behavior. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
def normalize(names: list[str]) -> list[str]:
    return [name.strip().title() for name in names]

print(normalize(["  nikhil", "PRIYA "]))
```

## Advanced Python example
```python
from typing import TypedDict

class Config(TypedDict):
    retries: int
    timeout: float

config: Config = {"retries": 3, "timeout": 1.5}
print(config["retries"])
```

## Detailed explanation
Type hints improve readability and tooling without changing runtime behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Type hints` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Type hints`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- ['Nikhil', 'Priya']
- 3
"""

from __future__ import annotations


def simple_python_example() -> None:
    def normalize(names: list[str]) -> list[str]:
        return [name.strip().title() for name in names]

    print(normalize(["  nikhil", "PRIYA "]))


def advanced_python_example() -> None:
    from typing import TypedDict

    class Config(TypedDict):
        retries: int
        timeout: float

    config: Config = {"retries": 3, "timeout": 1.5}
    print(config["retries"])


def main() -> None:
    print("=== 26. Type hints ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
