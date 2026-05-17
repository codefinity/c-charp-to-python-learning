# 2. Extended Unpacking

## Concept summary
Extended unpacking lets you split a sequence into head, middle, and tail in one statement.
The starred target (`*middle`) captures all remaining elements as a list.

## What C# developers usually expect
In C#, this usually needs index access, slicing helpers, or manual loops.
Python provides this directly in assignment syntax.

## How this example works
The list `[10, 20, 30, 40, 50]` is unpacked into:
`first = 10`
`middle = [20, 30, 40]`
`last = 50`
This is declarative and avoids error-prone index math.

## Why this matters in production
It improves readability for parsing tokens, handling path parts, splitting CLI arguments, and deconstructing structured values.
It also communicates intent clearly: one item at start, one at end, everything else in the middle.

## Common mistakes
Forgetting that the starred variable becomes a list.
Assuming unpacking tolerates mismatched shapes; if required elements are missing, Python raises `ValueError`.
Overusing unpacking in very complex patterns can hurt readability.

## Source
- [feature_02_extended_unpacking.py](../../src/csharp_to_python_learning/python_only_features/feature_02_extended_unpacking.py)

## Exact example from code file
```python
def main() -> None:
    first, *middle, last = [10, 20, 30, 40, 50]
    print(first, middle, last)


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_02_extended_unpacking.py
```

## Expected output
- `10 [20, 30, 40] 50`




