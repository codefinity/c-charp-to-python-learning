"""
# 54. Exception groups and `except*`

## What C# developers usually expect
C# developers usually expect one exception instance per `catch` flow.

## C# example
```csharp
try { Run(); }
catch (ValidationException ex) { ... }
catch (TimeoutException ex) { ... }
```

## Python equivalent
Python can raise multiple failures together with `ExceptionGroup` and handle each subtype with `except*`.

## Simple Python example
```python
raise ExceptionGroup("validation", [ValueError("bad id"), TypeError("bad kind")])
```

## Advanced Python example
```python
except* ValueError as group:
    print(len(group.exceptions))
```

## Detailed explanation
This is useful in concurrent code where multiple tasks fail and you need partial handling.

## Common mistakes for C# developers
1. Using plain `except` when `except*` is required.
2. Assuming one handler consumes the full grouped failure.

## Exercises
1. Build an `ExceptionGroup` with three exception types and handle each branch.
2. Re-raise unhandled branches and log them separately.

## Expected output
- value errors: 1
- type errors: 1
"""

from __future__ import annotations


def build_group() -> None:
    raise ExceptionGroup(
        "validation failures",
        [ValueError("bad id"), TypeError("bad kind"), ValueError("bad region")],
    )


def simple_python_example() -> None:
    try:
        build_group()
    except* ValueError as group:
        print(f"value errors: {len(group.exceptions)}")
    except* TypeError as group:
        print(f"type errors: {len(group.exceptions)}")


def advanced_python_example() -> None:
    try:
        raise ExceptionGroup(
            "task errors",
            [RuntimeError("retry"), TimeoutError("slow endpoint"), RuntimeError("retry again")],
        )
    except* RuntimeError as group:
        messages = [str(item) for item in group.exceptions]
        print(f"runtime branch: {messages}")
    except* TimeoutError as group:
        print(f"timeouts: {len(group.exceptions)}")


def main() -> None:
    print("=== 54. Exception groups and `except*` ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
