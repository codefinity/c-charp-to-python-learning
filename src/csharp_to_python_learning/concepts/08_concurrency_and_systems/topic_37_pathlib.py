"""
# 37. pathlib

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: `pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from pathlib import Path
path = Path("src") / "csharp_to_python_learning"
print(path.parts[0], path.name)
```

## Advanced Python example
```python
from pathlib import Path
python_files = list(Path("src").rglob("*.py"))
print(len(python_files) > 0)
```

## Detailed explanation
`pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `pathlib` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `pathlib`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- src csharp_to_python_learning
- True
"""

from __future__ import annotations


def simple_python_example() -> None:
    from pathlib import Path

    path = Path("src") / "csharp_to_python_learning"
    print(path.parts[0], path.name)


def advanced_python_example() -> None:
    from pathlib import Path

    python_files = list(Path("src").rglob("*.py"))
    print(len(python_files) > 0)


def main() -> None:
    print("=== 37. pathlib ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
