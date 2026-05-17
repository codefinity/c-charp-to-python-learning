"""
# 32. Async and await

## What C# developers usually expect
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

## C# example
```csharp
static async Task<string> FetchAsync()
{
    await Task.Delay(10);
    return "done";
}
```

## Python equivalent
Python approaches this concept with less ceremony: Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import asyncio

async def work():
    await asyncio.sleep(0)
    return "done"

print(asyncio.run(work()))
```

## Advanced Python example
```python
import asyncio

async def fetch(label: str, delay: float):
    await asyncio.sleep(delay)
    return label

async def main_async():
    result = await asyncio.gather(fetch("a", 0.01), fetch("b", 0.01))
    print(result)

asyncio.run(main_async())
```

## Detailed explanation
Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Async and await` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Async and await`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- done
- ['a', 'b']
"""

from __future__ import annotations


def simple_python_example() -> None:
    import asyncio

    async def work():
        await asyncio.sleep(0)
        return "done"

    print(asyncio.run(work()))


def advanced_python_example() -> None:
    import asyncio

    async def fetch(label: str, delay: float):
        await asyncio.sleep(delay)
        return label

    async def main_async():
        result = await asyncio.gather(fetch("a", 0.01), fetch("b", 0.01))
        print(result)

    asyncio.run(main_async())


def main() -> None:
    print("=== 32. Async and await ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
