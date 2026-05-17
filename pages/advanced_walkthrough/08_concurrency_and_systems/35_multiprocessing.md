### 35. Multiprocessing
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var values = new[] { 1, 2, 3 }.AsParallel().Select(n => n * n).ToArray();
Console.WriteLine($"[{string.Join(", ", values)}]");
```

Advanced equivalent:
```csharp
var queue = new System.Collections.Concurrent.BlockingCollection<int>();
var processLike = Task.Run(() => queue.Add(42));
await processLike;
Console.WriteLine(queue.Take());
```

**Simple Python example from this file**
```python
with Pool(2) as pool:
    print(pool.map(_square, [1, 2, 3]))
```

**Advanced Python example from this file**
```python
queue: Queue[int] = Queue()
process = Process(target=_publish_answer, args=(queue,))
process.start()
process.join()
print(queue.get())
```

**Python equivalent**
Python approaches this concept with less ceremony: Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Multiprocessing` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Multiprocessing`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 4, 9]
- 42
