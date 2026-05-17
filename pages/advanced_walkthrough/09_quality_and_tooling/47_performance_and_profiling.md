### 47. Performance and profiling
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var sw = System.Diagnostics.Stopwatch.StartNew();
for (var i = 0; i < 1000; i++) _ = Enumerable.Range(0, 1000).Sum();
sw.Stop();
Console.WriteLine(sw.ElapsedMilliseconds > 0);
```

Advanced equivalent:
```csharp
var sw = System.Diagnostics.Stopwatch.StartNew();
_ = Enumerable.Range(0, 20_000).Sum();
sw.Stop();
Console.WriteLine(sw.ElapsedMilliseconds >= 0);
```

**Simple Python example from this file**
```python
import timeit

duration = timeit.timeit("sum(range(1000))", number=1000)
print(duration > 0)
```

**Advanced Python example from this file**
```python
import cProfile
import io
import pstats

profile = cProfile.Profile()
profile.enable()
sum(range(20_000))
profile.disable()
stream = io.StringIO()
pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(1)
print("function calls" in stream.getvalue())
```

**Python equivalent**
Python approaches this concept with less ceremony: Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Performance and profiling` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Performance and profiling`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True
