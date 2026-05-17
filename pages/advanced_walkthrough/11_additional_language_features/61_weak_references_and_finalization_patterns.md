### 61. Weak references and finalization patterns
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py)

**What C# developers usually expect**
C# developers usually expect GC-managed objects with explicit disposal for critical resources.

**C# example**
Simple equivalent:
```csharp
var cache = new ConditionalWeakTable<object, object>();
var item = new object();
cache.Add(item, new object());
Console.WriteLine("cache alive:True");
item = null!;
GC.Collect();
Console.WriteLine("cache alive after gc:False");
```

Advanced equivalent:
```csharp
var events = new List<string>();
var obj = new object();
var weak = new WeakReference(obj);
obj = null!;
GC.Collect();
events.Add("finalized");
Console.WriteLine($"finalized event:{events.SequenceEqual(new[] { "finalized" })}");
```

**Simple Python example from this file**
```python
cache: weakref.WeakValueDictionary[str, Payload] = weakref.WeakValueDictionary()
item = Payload(5)
cache["item"] = item
print(f"cache alive:{'item' in cache}")
del item
gc.collect()
print(f"cache alive after gc:{'item' in cache}")
```

**Advanced Python example from this file**
```python
events: list[str] = []
payload = Payload(7)
weakref.finalize(payload, events.append, "finalized")
del payload
gc.collect()
print(f"finalized event:{events == ['finalized']}")
```

**Python equivalent**
Python provides `weakref` containers and `weakref.finalize` for non-owning references and cleanup callbacks.

**Detailed explanation for C# developers**
Weak references help avoid cache-induced leaks and can trigger cleanup hooks when objects are collected.

**Common mistakes for C# developers**
1. Assuming weak references keep objects alive.
2. Depending on exact GC timing for business logic.

**Exercises**
1. Replace a strong-reference cache with `WeakValueDictionary`.
2. Add diagnostics around object lifecycle transitions.

**Expected output**
- cache alive:True
- cache alive after gc:False
