"""
# 17. Modules and packages

## What C# developers usually expect
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import json
payload = json.loads('{"status":"ok"}')
print(payload["status"])
```

## Advanced Python example
```python
import importlib
module = importlib.import_module("statistics")
print(module.mean([2, 4, 8]))
```

## Detailed explanation
A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Modules and packages` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Modules and packages`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- ok
- 4.666
"""

from __future__ import annotations


def simple_python_example() -> None:
    import json

    payload = json.loads('{"status":"ok"}')
    print(payload["status"])


def advanced_python_example() -> None:
    import importlib

    module = importlib.import_module("statistics")
    print(module.mean([2, 4, 8]))


def main() -> None:
    print("=== 17. Modules and packages ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
