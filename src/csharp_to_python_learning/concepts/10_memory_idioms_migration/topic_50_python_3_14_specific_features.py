"""
# 50. Python 3.14-specific features

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var user = new Dictionary<string, string> { ["name"] = "Nikhil" };
Console.WriteLine(user["name"]);
```

Advanced equivalent:
```csharp
var features = new Dictionary<string, bool>
{
    ["deferred-annotations-like"] = true,
    ["free-threaded-support-like"] = true,
};
Console.WriteLine(features);
```

## Python equivalent
Python approaches this concept with less ceremony: Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from __future__ import annotations

def build_user(name: "str") -> "dict[str, str]":
    return {"name": name}

print(build_user("Nikhil")["name"])
```

## Advanced Python example
```python
import importlib.util

features = {
    "annotationlib": importlib.util.find_spec("annotationlib") is not None,
    "compression.zstd": importlib.util.find_spec("compression.zstd") is not None,
}
print(features)
```

## Detailed explanation
Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Python 3.14-specific features` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Python 3.14-specific features`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- Nikhil
- {'annotationlib':

## Further Study
Read the official 3.14 What's New document to track point-release changes in 3.14.x.
"""

from __future__ import annotations


def simple_python_example() -> None:
    def build_user(name: str) -> dict[str, str]:
        return {"name": name}

    print(build_user("Nikhil")["name"])


def advanced_python_example() -> None:
    import importlib.util

    features = {
        "annotationlib": importlib.util.find_spec("annotationlib") is not None,
        "compression.zstd": importlib.util.find_spec("compression.zstd") is not None,
    }
    print(features)


def main() -> None:
    print("=== 50. Python 3.14-specific features ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
