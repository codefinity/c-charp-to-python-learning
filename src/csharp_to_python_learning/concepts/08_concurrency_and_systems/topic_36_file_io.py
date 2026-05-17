"""
# 36. File I/O

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Prefer explicit encodings and context managers for reliable file handling in production. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "sample.txt"
    path.write_text("hello", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
```

## Advanced Python example
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.log"
    with path.open("w", encoding="utf-8") as file:
        for index in range(3):
            file.write(f"line-{index}\n")
    print(path.read_text(encoding="utf-8").strip().splitlines()[-1])
```

## Detailed explanation
Prefer explicit encodings and context managers for reliable file handling in production. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `File I/O` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `File I/O`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- hello
- line-2
"""

from __future__ import annotations


def simple_python_example() -> None:
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        path = Path(directory) / "sample.txt"
        path.write_text("hello", encoding="utf-8")
        print(path.read_text(encoding="utf-8"))


def advanced_python_example() -> None:
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        path = Path(directory) / "data.log"
        with path.open("w", encoding="utf-8") as file:
            for index in range(3):
                file.write(f"line-{index}\n")
        print(path.read_text(encoding="utf-8").strip().splitlines()[-1])


def main() -> None:
    print("=== 36. File I/O ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
