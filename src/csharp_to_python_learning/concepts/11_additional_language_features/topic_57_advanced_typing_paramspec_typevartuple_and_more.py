"""
# 57. Advanced typing: `ParamSpec`, `TypeVarTuple`, `Literal`, `Annotated`, `Self`

## What C# developers usually expect
C# developers usually expect compile-time generic metadata and fluent APIs with strong type flow.

## C# example
```csharp
public TOut Wrap<TIn, TOut>(Func<TIn, TOut> func) => ...
```

## Python equivalent
Python typing can express callable signatures (`ParamSpec`), variadic generic shapes (`TypeVarTuple`), value-level modes (`Literal`), metadata (`Annotated`), and fluent `Self`.

## Simple Python example
```python
@traced
def add(x: int, y: int) -> int:
    return x + y
```

## Advanced Python example
```python
row = Row[int, str](10, "ok")
query = Query().where("status").where("region")
```

## Detailed explanation
These hints improve editor accuracy, API contracts, and static checks without changing runtime semantics.

## Common mistakes for C# developers
1. Expecting type hints to enforce runtime behavior automatically.
2. Ignoring value-level contracts where `Literal` improves safety.

## Exercises
1. Convert one decorator-heavy helper to use `ParamSpec`.
2. Add `Literal` modes to one public API.

## Expected output
- traced:add
- row:(10, 'ok')
"""

from __future__ import annotations

from collections.abc import Callable
from typing import (
    Annotated,
    Generic,
    Literal,
    ParamSpec,
    Self,
    TypeVar,
    TypeVarTuple,
    Unpack,
)

P = ParamSpec("P")
R = TypeVar("R")
Ts = TypeVarTuple("Ts")
Mode = Literal["fast", "safe"]


def traced(func: Callable[P, R]) -> Callable[P, R]:  # noqa: UP047
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"traced:{func.__name__}")
        return func(*args, **kwargs)

    return wrapper


class Row(Generic[Unpack[Ts]]):  # noqa: UP044, UP046
    def __init__(self, *values: Unpack[Ts]) -> None:  # noqa: UP044
        self.values: tuple[Unpack[Ts]] = values  # noqa: UP044


class Query:
    def __init__(self) -> None:
        self.filters: list[str] = []

    def where(self, field: str) -> Self:
        self.filters.append(field)
        return self


def fetch(mode: Mode, port: Annotated[int, "tcp-port"]) -> str:
    return f"{mode}@{port}"


def simple_python_example() -> None:
    @traced
    def add(x: int, y: int) -> int:
        return x + y

    print(add(2, 3))


def advanced_python_example() -> None:
    row = Row[int, str](10, "ok")
    print(f"row:{row.values}")
    query = Query().where("status").where("region")
    print(f"filters:{query.filters}")
    print(fetch("safe", 443))


def main() -> None:
    print(
        "=== 57. Advanced typing: `ParamSpec`, `TypeVarTuple`, `Literal`, `Annotated`, `Self` ==="
    )
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
