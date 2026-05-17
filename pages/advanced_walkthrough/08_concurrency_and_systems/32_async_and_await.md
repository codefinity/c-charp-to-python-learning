### 32. Async and await
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py)

**What C# developers usually expect**
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

**C# example**
Simple equivalent:
```csharp
static async Task<string> Work()
{
    await Task.Yield();
    return "done";
}
Console.WriteLine(await Work());
```

Advanced equivalent:
```csharp
static async Task<string> Fetch(string label, int delayMs)
{
    await Task.Delay(delayMs);
    return label;
}
var result = await Task.WhenAll(Fetch("a", 10), Fetch("b", 10));
Console.WriteLine($"[{string.Join(", ", result)}]");
```

**Simple Python example from this file**
```python
import asyncio

async def work():
    await asyncio.sleep(0)
    return "done"

print(asyncio.run(work()))
```

**Advanced Python example from this file**
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

**Python equivalent**
Python approaches this concept with less ceremony: Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Async and await` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Async and await`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- done
- ['a', 'b']
