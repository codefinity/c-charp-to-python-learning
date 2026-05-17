### 52. Common C# to Python migration mistakes
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
static readonly List<int> Shared = new();
static List<int> AppendBad(int item)
{
    Shared.Add(item);
    return Shared;
}
Console.WriteLine($"[{string.Join(", ", AppendBad(1))}] [{string.Join(", ", AppendBad(2))}]");
```

Advanced equivalent:
```csharp
static List<int> AppendGood(int item, List<int>? bucket = null)
{
    bucket ??= new List<int>();
    bucket.Add(item);
    return bucket;
}
Console.WriteLine($"[{string.Join(", ", AppendGood(1))}] [{string.Join(", ", AppendGood(2))}]");
```

**Simple Python example from this file**
```python
def append_bad(item, bucket=[]):  # noqa: B006 - intentional pitfall demo
    bucket.append(item)
    return bucket

print(append_bad(1), append_bad(2))
```

**Advanced Python example from this file**
```python
def append_good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket

print(append_good(1), append_good(2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Common C# to Python migration mistakes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Common C# to Python migration mistakes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 2]
- [1] [2]
