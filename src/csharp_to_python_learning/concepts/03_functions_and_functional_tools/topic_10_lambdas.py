"""
# 10. Lambdas

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var teams = new[] { "platform", "api", "ml" };
var ordered = teams.OrderBy(t => t.Length);
Console.WriteLine($"[{string.Join(", ", ordered)}]");
```

Advanced equivalent:
```csharp
var records = new[]
{
    new { Name = "A", Score = 92 },
    new { Name = "B", Score = 81 },
};
var top = records.OrderByDescending(r => r.Score).ThenBy(r => r.Name).First();
Console.WriteLine($"{top.Name} {top.Score}");
```

## Python equivalent
Python approaches this concept with less ceremony: Python lambdas are small expression-only functions, best used inline for short transformations. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
teams = ["platform", "api", "ml"]
print(sorted(teams, key=lambda t: len(t)))
```

## Advanced Python example
```python
records = [{"name": "A", "score": 92}, {"name": "B", "score": 81}]
top = max(records, key=lambda r: (r["score"], r["name"]))
print(top["name"], top["score"])
```

## Detailed explanation
Python lambdas are small expression-only functions, best used inline for short transformations. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Lambdas` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Lambdas`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- ['ml', 'api', 'platform']
- A 92
"""

from __future__ import annotations


def simple_python_example() -> None:
    teams = ["platform", "api", "ml"]
    print(sorted(teams, key=lambda t: len(t)))


def advanced_python_example() -> None:
    records = [{"name": "A", "score": 92}, {"name": "B", "score": 81}]
    top = max(records, key=lambda r: (r["score"], r["name"]))
    print(top["name"], top["score"])


def main() -> None:
    print("=== 10. Lambdas ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
