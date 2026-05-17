### 51. Python idioms versus C# idioms
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var numbers = new[] { 1, 2, 3, 4 };
var evens = numbers.Where(n => n % 2 == 0).ToList();
Console.WriteLine($"[{string.Join(", ", evens)}]");
```

Advanced equivalent:
```csharp
var records = new[] { new { Name = "a", Score = 10 }, new { Name = "b", Score = 7 } };
var best = records.OrderByDescending(r => r.Score).First();
Console.WriteLine(best.Name);
```

**Simple Python example from this file**
```python
numbers = [1, 2, 3, 4]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

**Advanced Python example from this file**
```python
from typing import TypedDict

class ScoreRecord(TypedDict):
    name: str
    score: int

records: list[ScoreRecord] = [{"name": "a", "score": 10}, {"name": "b", "score": 7}]
best = max(records, key=lambda r: r["score"])
print(best["name"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Translate intent, not syntax: many C# patterns have shorter Pythonic forms. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Translate intent, not syntax: many C# patterns have shorter Pythonic forms. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python idioms versus C# idioms` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python idioms versus C# idioms`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [2, 4]
- a
