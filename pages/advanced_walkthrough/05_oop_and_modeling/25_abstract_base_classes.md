### 25. Abstract base classes
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
abstract class Repository { public abstract string Get(string key); }
class InMemoryRepository : Repository { public override string Get(string key) => $"value:{key}"; }
Console.WriteLine(new InMemoryRepository().Get("x"));
```

Advanced equivalent:
```csharp
class CsvLike : IEnumerable<string>
{
    public IEnumerator<string> GetEnumerator() { yield return "a,b"; yield return "c,d"; }
    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
}
Console.WriteLine(new CsvLike() is IEnumerable<string>);
```

**Simple Python example from this file**
```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, key: str) -> str: ...

class InMemoryRepository(Repository):
    def get(self, key: str) -> str:
        return f"value:{key}"

print(InMemoryRepository().get("x"))
```

**Advanced Python example from this file**
```python
from collections.abc import Iterable

class CsvLike:
    def __iter__(self):
        yield from ["a,b", "c,d"]

print(isinstance(CsvLike(), Iterable))
```

**Python equivalent**
Python approaches this concept with less ceremony: ABCs define explicit contracts and can also provide reusable default behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
ABCs define explicit contracts and can also provide reusable default behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Abstract base classes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Abstract base classes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- value:x
- True
