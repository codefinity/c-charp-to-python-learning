"""
# 15. Context managers

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from contextlib import contextmanager

@contextmanager
def labelled(name: str):
    print(f"enter {name}")
    try:
        yield
    finally:
        print(f"exit {name}")

with labelled("demo"):
    print("inside")
```

## Advanced Python example
```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "note.txt"
    path.write_text("safe write", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
```

## Detailed explanation
Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Context managers` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Context managers`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- enter demo
- safe write
"""

from __future__ import annotations


def simple_python_example() -> None:
    from contextlib import contextmanager

    @contextmanager
    def labelled(name: str):
        print(f"enter {name}")
        try:
            yield
        finally:
            print(f"exit {name}")

    with labelled("demo"):
        print("inside")


def advanced_python_example() -> None:
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "note.txt"
        path.write_text("safe write", encoding="utf-8")
        print(path.read_text(encoding="utf-8"))


def main() -> None:
    print("=== 15. Context managers ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
