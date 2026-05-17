"""
# 3. Variables, names, references, and mutability

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
a = [1, 2]
b = a
b.append(3)
print(a, b)
```

## Advanced Python example
```python
original = {"region": "APAC", "skills": ["C#", "SQL"]}
copy_for_edit = {**original, "skills": [*original["skills"], "Python"]}
print(original)
print(copy_for_edit)
```

## Detailed explanation
Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Variables, names, references, and mutability` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Variables, names, references, and mutability`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- [1, 2, 3] [1, 2, 3]
- {'region': 'APAC', 'skills': ['C#', 'SQL']}
"""

from __future__ import annotations


def simple_python_example() -> None:
    a = [1, 2]
    b = a
    b.append(3)
    print(a, b)


def advanced_python_example() -> None:
    original = {"region": "APAC", "skills": ["C#", "SQL"]}
    copy_for_edit = {**original, "skills": [*original["skills"], "Python"]}
    print(original)
    print(copy_for_edit)


def main() -> None:
    print("=== 3. Variables, names, references, and mutability ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
