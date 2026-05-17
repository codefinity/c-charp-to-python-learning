### 54. Exception groups and `except*`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py)

**What C# developers usually expect**
C# developers usually expect one exception instance per `catch` flow.

**C# example**
Simple equivalent:
```csharp
try
{
    throw new AggregateException(new FormatException("bad id"), new InvalidCastException("bad kind"));
}
catch (AggregateException ex)
{
    Console.WriteLine($"value errors: {ex.InnerExceptions.Count(e => e is FormatException)}");
    Console.WriteLine($"type errors: {ex.InnerExceptions.Count(e => e is InvalidCastException)}");
}
```

Advanced equivalent:
```csharp
try
{
    throw new AggregateException(new InvalidOperationException("retry"), new TimeoutException("slow endpoint"));
}
catch (AggregateException ex)
{
    Console.WriteLine($"runtime branch: [{string.Join(", ", ex.InnerExceptions.OfType<InvalidOperationException>().Select(e => e.Message))}]");
    Console.WriteLine($"timeouts: {ex.InnerExceptions.Count(e => e is TimeoutException)}");
}
```

**Simple Python example from this file**
```python
try:
    build_group()
except* ValueError as group:
    print(f"value errors: {len(group.exceptions)}")
except* TypeError as group:
    print(f"type errors: {len(group.exceptions)}")
```

**Advanced Python example from this file**
```python
try:
    raise ExceptionGroup(
        "task errors",
        [RuntimeError("retry"), TimeoutError("slow endpoint"), RuntimeError("retry again")],
    )
except* RuntimeError as group:
    messages = [str(item) for item in group.exceptions]
    print(f"runtime branch: {messages}")
except* TimeoutError as group:
    print(f"timeouts: {len(group.exceptions)}")
```

**Python equivalent**
Python can raise multiple failures together with `ExceptionGroup` and handle each subtype with `except*`.

**Detailed explanation for C# developers**
This is useful in concurrent code where multiple tasks fail and you need partial handling.

**Common mistakes for C# developers**
1. Using plain `except` when `except*` is required.
2. Assuming one handler consumes the full grouped failure.

**Exercises**
1. Build an `ExceptionGroup` with three exception types and handle each branch.
2. Re-raise unhandled branches and log them separately.

**Expected output**
- value errors: 1
- type errors: 1
