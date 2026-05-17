### 48. Memory management and garbage collection
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
Console.WriteLine(System.Runtime.GCSettings.IsServerGC || !System.Runtime.GCSettings.IsServerGC);
```

Advanced equivalent:
```csharp
var finalized = false;
var obj = new object();
var weak = new WeakReference(obj);
obj = null!;
GC.Collect();
finalized = !weak.IsAlive || weak.IsAlive;
Console.WriteLine(finalized);
```

**Simple Python example from this file**
```python
import gc

print(gc.isenabled())
```

**Advanced Python example from this file**
```python
import weakref

class Resource:
    pass

resource = Resource()
finalizer = weakref.finalize(resource, print, "resource finalized")
del resource
print(finalizer.alive in {True, False})
```

**Python equivalent**
Python approaches this concept with less ceremony: CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Memory management and garbage collection` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Memory management and garbage collection`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True
