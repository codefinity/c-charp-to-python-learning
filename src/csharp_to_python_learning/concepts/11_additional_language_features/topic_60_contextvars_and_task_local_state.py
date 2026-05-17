"""
# 60. `contextvars` and task-local state

## What C# developers usually expect
C# developers usually expect `AsyncLocal<T>` style correlation IDs across async call chains.

## C# example
```csharp
AsyncLocal<string> RequestId = new();
```

## Python equivalent
Python uses `contextvars.ContextVar` to carry per-task request context safely in async workflows.

## Simple Python example
```python
request_id.set("req-101")
```

## Advanced Python example
```python
await asyncio.gather(handle("a"), handle("b"))
```

## Detailed explanation
Use `contextvars` for trace IDs, tenant IDs, and auth context when concurrent tasks share execution threads.

## Common mistakes for C# developers
1. Storing request state in global variables.
2. Assuming normal module globals are task-isolated.

## Exercises
1. Add a request-id context var to one async pipeline.
2. Propagate context into logging formatters.

## Expected output
- req:sync-1
- ['task-a', 'task-b']
"""

from __future__ import annotations

import asyncio
from contextvars import ContextVar, Token

request_id: ContextVar[str] = ContextVar("request_id", default="missing")


def simple_python_example() -> None:
    token: Token[str] = request_id.set("sync-1")
    try:
        print(f"req:{request_id.get()}")
    finally:
        request_id.reset(token)


async def handle(name: str) -> str:
    token = request_id.set(f"task-{name}")
    try:
        await asyncio.sleep(0)
        return request_id.get()
    finally:
        request_id.reset(token)


async def advanced_python_example() -> None:
    values = await asyncio.gather(handle("a"), handle("b"))
    print(values)


async def main_async() -> None:
    print("=== 60. `contextvars` and task-local state ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    await advanced_python_example()


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
