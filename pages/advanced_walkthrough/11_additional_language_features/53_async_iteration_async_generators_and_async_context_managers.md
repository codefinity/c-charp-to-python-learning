### 53. Async iteration, async generators, and async context managers
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py)

**What C# developers usually expect**
C# developers usually expect `await foreach` and `await using` for asynchronous streaming and cleanup.

**C# example**
Simple equivalent:
```csharp
static async IAsyncEnumerable<int> StreamNumbers(int limit = 3)
{
    for (var i = 0; i < limit; i++) { await Task.Yield(); yield return i; }
}
await foreach (var value in StreamNumbers()) Console.WriteLine(value);
```

Advanced equivalent:
```csharp
sealed class AsyncScope : IAsyncDisposable
{
    private readonly string _name;
    public AsyncScope(string name) { _name = name; Console.WriteLine($"enter:{name}"); }
    public ValueTask DisposeAsync() { Console.WriteLine($"exit:{_name}"); return ValueTask.CompletedTask; }
}
await using (new AsyncScope("pipeline"))
{
    var squares = new List<int>();
    await foreach (var value in StreamNumbers()) squares.Add(value * value);
    Console.WriteLine($"squares:[{string.Join(", ", squares)}]");
}
```

**Simple Python example from this file**
```python
async for value in stream_numbers():
    print(value)
```

**Advanced Python example from this file**
```python
async with traced_scope("pipeline"):
    squares = [value * value async for value in stream_numbers()]
    print(f"squares:{squares}")
```

**Python equivalent**
Python uses `async for`, async generators, async comprehensions, and `async with` to model the same patterns.

**Detailed explanation for C# developers**
Use `async for` when values arrive over time, and `async with` when setup/cleanup must also await I/O.

**Common mistakes for C# developers**
1. Treating async generators like regular lists.
2. Forgetting that async context managers require `async with`, not `with`.

**Exercises**
1. Convert a synchronous generator pipeline to an async pipeline.
2. Add timing logs with an async context manager.

**Expected output**
- enter:pipeline
- squares:[0, 1, 4]
