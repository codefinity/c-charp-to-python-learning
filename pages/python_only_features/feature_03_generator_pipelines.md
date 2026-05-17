# 3. Generator Pipelines

## Concept summary
Generator pipelines process data lazily.
Values are produced only when requested, which keeps memory usage low and composes naturally.

## What C# developers usually expect
This feels similar to LINQ over `IEnumerable<T>`, but Python generator syntax is built directly into the language.
`yield`, generator expressions, and `yield from` make stream pipelines concise.

## How this example works
`numbers()` yields `0..4` lazily.
`pipeline()` returns a generator expression that filters even numbers and squares them.
No list is created inside `pipeline`; it creates an iterator pipeline.
`list(pipeline())` in `main` materializes the final output for printing.

## Why this matters in production
This pattern is useful for ETL, log processing, and large file processing where loading everything at once is expensive.
You can chain filters and transforms while keeping code readable.

## Common mistakes
Assuming generators can be iterated repeatedly like lists.
Once consumed, a generator is exhausted.
Another mistake is forcing `list(...)` too early, which removes laziness.

## Source
- [feature_03_generator_pipelines.py](../../src/csharp_to_python_learning/python_only_features/feature_03_generator_pipelines.py)

## Exact example from code file
```python
def numbers():
    yield from range(5)


def pipeline():
    return (value * value for value in numbers() if value % 2 == 0)


def main() -> None:
    print(list(pipeline()))


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_03_generator_pipelines.py
```

## Expected output
- `[0, 4, 16]`




