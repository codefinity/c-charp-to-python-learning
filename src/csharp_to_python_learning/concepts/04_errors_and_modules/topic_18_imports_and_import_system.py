"""
# 18. Imports and import system

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var pathlibLike = typeof(Path);
Console.WriteLine(pathlibLike is not null);
```

Advanced equivalent:
```csharp
string LazyJson()
{
    return System.Text.Json.JsonSerializer.Serialize(new { lazy = true });
}
Console.WriteLine(LazyJson());
```

## Python equivalent
Python approaches this concept with less ceremony: Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import importlib.util
spec = importlib.util.find_spec("pathlib")
print(spec is not None)
```

## Advanced Python example
```python
def lazy_json():
    import json
    return json.dumps({"lazy": True})

print(lazy_json())
```

## Detailed explanation
Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Imports and import system` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Imports and import system`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- True
- {"lazy": true}
"""

from __future__ import annotations


def simple_python_example() -> None:
    import importlib.util

    spec = importlib.util.find_spec("pathlib")
    print(spec is not None)


def advanced_python_example() -> None:
    def lazy_json():
        import json

        return json.dumps({"lazy": True})

    print(lazy_json())


def main() -> None:
    print("=== 18. Imports and import system ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
