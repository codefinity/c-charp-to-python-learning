### 49. Standard library overview
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
Console.WriteLine(Math.Round(new[] { 10.0, 20.0, 40.0 }.Average(), 2));
```

Advanced equivalent:
```csharp
var pairs = new[] { 1, 2, 3, 4 }.Zip(new[] { 2, 3, 4, 5 }, (a, b) => (a, b)).ToList();
Console.WriteLine(pairs.Last());
```

**Simple Python example from this file**
```python
import statistics

print(round(statistics.mean([10, 20, 40]), 2))
```

**Advanced Python example from this file**
```python
from itertools import pairwise

pairs = list(pairwise([1, 2, 3, 4]))
print(pairs[-1])
```

**Python equivalent**
Python approaches this concept with less ceremony: The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Standard library overview` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Standard library overview`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 23.33
- (3, 4)
