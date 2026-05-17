# 6. Structural Pattern Matching

## Concept summary
Structural pattern matching (`match` / `case`) branches on data shape and values together.
It can inspect dictionaries, sequences, class patterns, and guards in one construct.

## What C# developers usually expect
C# `switch` and pattern matching are familiar, but Python emphasizes structural deconstruction of runtime data (especially dictionaries/lists) with concise syntax.

## How this example works
The function matches an incoming dictionary.
Case 1: `{"kind": "http", "status": status}` with guard `status >= 500` returns `server-error`.
Case 2: same shape without the guard returns `http-{status}`.
Fallback case `_` returns `unknown`.
Input `{"kind": "http", "status": 503}` matches the guarded case first.

## Why this matters in production
This style is useful for event routers, message handlers, protocol parsers, and API response classification.
It reduces nested `if`/`elif` trees and keeps matching logic declarative.

## Common mistakes
Assuming match is only value equality.
Order matters: first matching case wins.
Overusing very complex patterns can hurt readability; keep patterns focused.

## Source
- [feature_06_pattern_matching.py](../../src/csharp_to_python_learning/python_only_features/feature_06_pattern_matching.py)

## Exact example from code file
```python
def describe(value):
    match value:
        case {"kind": "http", "status": status} if status >= 500:
            return "server-error"
        case {"kind": "http", "status": status}:
            return f"http-{status}"
        case _:
            return "unknown"


def main() -> None:
    print(describe({"kind": "http", "status": 503}))


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_06_pattern_matching.py
```

## Expected output
- `server-error`




