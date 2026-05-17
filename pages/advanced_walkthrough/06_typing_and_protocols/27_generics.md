### 27. Generics
Source: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
Simple equivalent:
```csharp
class Box<T> { public T Value { get; } public Box(T value) => Value = value; }
Console.WriteLine(new Box<int>(10).Value);
```

Advanced equivalent:
```csharp
static T First<T>(List<T> items) => items[0];
Console.WriteLine(First(new List<string> { "a", "b", "c" }));
```

**Simple Python example from this file**
```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

print(Box[int](10).value)
```

**Advanced Python example from this file**
```python
from typing import TypeVar

U = TypeVar("U")

def first(items: list[U]) -> U:
    return items[0]

print(first(["a", "b", "c"]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python generics are type-checker friendly and map closely to C# generic classes and methods. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python generics are type-checker friendly and map closely to C# generic classes and methods. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Generics` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Generics`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 10
- a
