# 4. Contextlib Context Managers

## Concept summary
`contextlib.contextmanager` lets you define `with`-block behavior using a function with `yield`.
Code before `yield` runs on enter, and code in `finally` runs on exit.

## What C# developers usually expect
In C#, this is closest to `using` / `IDisposable` lifecycle control.
Python can do class-based context managers too, but `@contextmanager` provides a compact function-based style.

## How this example works
`banner("deploy")` prints `start:deploy`, then yields control to the `with` block.
Inside the block, `inside` is printed.
When the block exits, the `finally` section runs and prints `end:deploy`.
This happens even if an exception occurs inside the block.

## Why this matters in production
Use this for setup/cleanup boundaries such as timing, tracing, temporary environment changes, lock management, or transactional wrappers.
It keeps resource and lifecycle logic centralized.

## Common mistakes
Forgetting `try/finally` around `yield`, which can skip cleanup on errors.
Putting too much business logic inside the context manager instead of keeping it focused on lifecycle concerns.

## Source
- [feature_04_contextlib_magic.py](../../src/csharp_to_python_learning/python_only_features/feature_04_contextlib_magic.py)

## Exact example from code file
```python
from contextlib import contextmanager


@contextmanager
def banner(label: str):
    print(f"start:{label}")
    try:
        yield
    finally:
        print(f"end:{label}")


def main() -> None:
    with banner("deploy"):
        print("inside")


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_04_contextlib_magic.py
```

## Expected output
- `start:deploy`
- `inside`
- `end:deploy`




