"""
# 33. asyncio tasks, queues, cancellation, timeouts

## What C# developers usually expect
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

## C# example
Simple equivalent:
```csharp
var channel = System.Threading.Channels.Channel.CreateUnbounded<int>();
_ = Task.Run(async () =>
{
    foreach (var value in new[] { 1, 2, 3 }) await channel.Writer.WriteAsync(value);
    channel.Writer.Complete();
});
await foreach (var item in channel.Reader.ReadAllAsync()) Console.WriteLine($"consumed {item}");
```

Advanced equivalent:
```csharp
var cts = new CancellationTokenSource(TimeSpan.FromMilliseconds(50));
try
{
    await Task.Delay(200, cts.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("timed out");
}
```

## Python equivalent
Python approaches this concept with less ceremony: Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import asyncio

async def producer(queue: asyncio.Queue[int]) -> None:
    for value in [1, 2, 3]:
        await queue.put(value)
    await queue.put(-1)

async def consumer(queue: asyncio.Queue[int]) -> None:
    while True:
        item = await queue.get()
        if item == -1:
            break
        print("consumed", item)

async def main_async():
    q: asyncio.Queue[int] = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main_async())
```

## Advanced Python example
```python
import asyncio

async def slow():
    await asyncio.sleep(0.2)
    return "slow"

async def main_async():
    try:
        await asyncio.wait_for(slow(), timeout=0.05)
    except TimeoutError:
        print("timed out")

asyncio.run(main_async())
```

## Detailed explanation
Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `asyncio tasks, queues, cancellation, timeouts` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `asyncio tasks, queues, cancellation, timeouts`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- consumed 1
- timed out
"""

from __future__ import annotations


def simple_python_example() -> None:
    import asyncio

    async def producer(queue: asyncio.Queue[int]) -> None:
        for value in [1, 2, 3]:
            await queue.put(value)
        await queue.put(-1)

    async def consumer(queue: asyncio.Queue[int]) -> None:
        while True:
            item = await queue.get()
            if item == -1:
                break
            print("consumed", item)

    async def main_async():
        q: asyncio.Queue[int] = asyncio.Queue()
        await asyncio.gather(producer(q), consumer(q))

    asyncio.run(main_async())


def advanced_python_example() -> None:
    import asyncio

    async def slow():
        await asyncio.sleep(0.2)
        return "slow"

    async def main_async():
        try:
            await asyncio.wait_for(slow(), timeout=0.05)
        except TimeoutError:
            print("timed out")

    asyncio.run(main_async())


def main() -> None:
    print("=== 33. asyncio tasks, queues, cancellation, timeouts ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
