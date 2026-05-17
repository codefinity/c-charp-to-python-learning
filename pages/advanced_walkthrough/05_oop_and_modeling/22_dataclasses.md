### 22. Dataclasses
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
record User(int Id, string Name);
Console.WriteLine(new User(1, "Nikhil"));
```

Advanced equivalent:
```csharp
record Job(int Priority, string Name, IReadOnlyList<string> Tags);
var first = new[] { new Job(2, "test", Array.Empty<string>()), new Job(1, "build", Array.Empty<string>()) }
    .OrderBy(j => j.Priority)
    .First();
Console.WriteLine(first.Name);
```

**Simple Python example from this file**
```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

print(User(1, "Nikhil"))
```

**Advanced Python example from this file**
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True, slots=True)
class Job:
    priority: int
    name: str
    tags: tuple[str, ...] = field(default_factory=tuple)

print(sorted([Job(2, "test"), Job(1, "build")])[0].name)
```

**Python equivalent**
Python approaches this concept with less ceremony: Dataclasses are concise record-like types with optional immutability, ordering, and slots. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Dataclasses are concise record-like types with optional immutability, ordering, and slots. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Dataclasses` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Dataclasses`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- User(id=1, name='Nikhil')
- build
