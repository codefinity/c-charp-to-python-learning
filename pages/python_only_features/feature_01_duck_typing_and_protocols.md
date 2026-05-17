# 1. Duck Typing and Protocols

## Concept summary
Duck typing means Python cares about what an object can do, not what it inherits from.
If an object has the required method, it can be used.
`Protocol` lets you document that expected shape for static type checkers.

## What C# developers usually expect
In C#, we normally model this with explicit interfaces and nominal typing.
Python can do that style too, but idiomatic code often accepts any object with the needed behavior.

## How this example works
`Writer` is a `Protocol` that says "anything with `write(self, text: str) -> str` is valid."
`ConsoleWriter` does not inherit from `Writer`, but it still matches because it has a compatible `write` method.
`publish` takes a `Writer` and calls `writer.write("pythonic")`.
At runtime, Python just calls the method. Static tools (`mypy`, `pyright`) use `Protocol` to check compatibility.

## Why this matters in production
This makes APIs extensible and testable.
You can pass real implementations, in-memory fakes, or test doubles without inheritance coupling.
It is especially useful for adapters and I/O boundaries.

## Common mistakes
Assuming `Protocol` enforces runtime checks by default.
It mainly helps static analysis unless you add explicit runtime validation.
Another mistake is overusing `Any` and losing the benefits of structural typing.

## Source
- [feature_01_duck_typing_and_protocols.py](../../src/csharp_to_python_learning/python_only_features/feature_01_duck_typing_and_protocols.py)

## Exact example from code file
```python
from typing import Protocol


class Writer(Protocol):
    def write(self, text: str) -> str: ...


class ConsoleWriter:
    def write(self, text: str) -> str:
        return text.upper()


def publish(writer: Writer) -> str:
    return writer.write("pythonic")


def main() -> None:
    print(publish(ConsoleWriter()))


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_01_duck_typing_and_protocols.py
```

## Expected output
- `PYTHONIC`




