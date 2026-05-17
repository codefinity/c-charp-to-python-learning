### 60. `contextvars` and task-local state
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py)

**What C# developers usually expect**
C# developers usually expect `AsyncLocal<T>` style correlation IDs across async call chains.

**C# example**
Simple equivalent:
```csharp
var requestId = new System.Threading.AsyncLocal<string>();
requestId.Value = "sync-1";
Console.WriteLine($"req:{requestId.Value}");
```

Advanced equivalent:
```csharp
var requestId = new System.Threading.AsyncLocal<string>();
async Task<string> Handle(string name)
{
    requestId.Value = $"task-{name}";
    await Task.Yield();
    return requestId.Value!;
}
var values = await Task.WhenAll(Handle("a"), Handle("b"));
Console.WriteLine($"[{string.Join(", ", values)}]");
```

**Simple Python example from this file**
```python
token: Token[str] = request_id.set("sync-1")
try:
    print(f"req:{request_id.get()}")
finally:
    request_id.reset(token)
```

**Advanced Python example from this file**
```python
values = await asyncio.gather(handle("a"), handle("b"))
print(values)
```

**Python equivalent**
Python uses `contextvars.ContextVar` to carry per-task request context safely in async workflows.

**Detailed explanation for C# developers**
Use `contextvars` for trace IDs, tenant IDs, and auth context when concurrent tasks share execution threads.

**Common mistakes for C# developers**
1. Storing request state in global variables.
2. Assuming normal module globals are task-isolated.

**Exercises**
1. Add a request-id context var to one async pipeline.
2. Propagate context into logging formatters.

**Expected output**
- req:sync-1
- ['task-a', 'task-b']
