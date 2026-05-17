"""
# 53. Async iteration, async generators, and async context managers

## What C# developers usually expect
C# developers usually expect `await foreach` and `await using` for asynchronous streaming and cleanup.

## C# example
```csharp
await foreach (var item in ReadAsync())
{
    Console.WriteLine(item);
}
```

## Python equivalent
Python uses `async for`, async generators, async comprehensions, and `async with` to model the same patterns.

## Simple Python example
```python
async for value in stream_numbers():
    print(value)
```

## Advanced Python example
```python
async with traced_scope("pipeline"):
    squares = [value * value async for value in stream_numbers()]
```

## Detailed explanation
Use `async for` when values arrive over time, and `async with` when setup/cleanup must also await I/O.

## Common mistakes for C# developers
1. Treating async generators like regular lists.
2. Forgetting that async context managers require `async with`, not `with`.

## Exercises
1. Convert a synchronous generator pipeline to an async pipeline.
2. Add timing logs with an async context manager.

## Expected output
- enter:pipeline
- squares:[0, 1, 4]
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager


async def stream_numbers(limit: int = 3) -> AsyncIterator[int]:
    for value in range(limit):
        await asyncio.sleep(0)
        yield value


@asynccontextmanager
async def traced_scope(name: str) -> AsyncIterator[None]:
    print(f"enter:{name}")
    try:
        yield
    finally:
        await asyncio.sleep(0)
        print(f"exit:{name}")


async def simple_python_example() -> None:
    async for value in stream_numbers():
        print(value)


async def advanced_python_example() -> None:
    async with traced_scope("pipeline"):
        squares = [value * value async for value in stream_numbers()]
        print(f"squares:{squares}")


async def main_async() -> None:
    print("=== 53. Async iteration, async generators, and async context managers ===")
    print("-- Simple Python example --")
    await simple_python_example()
    print("-- Advanced Python example --")
    await advanced_python_example()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
