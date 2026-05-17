### 28. Pattern matching
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
static string Classify(object value) => value switch
{
    0 => "zero",
    int n when n > 0 => "positive",
    _ => "other",
};
Console.WriteLine(Classify(3));
```

Advanced equivalent:
```csharp
record Event(string Kind, int Size);
static string Route(Event e) => e switch
{
    { Kind: "upload", Size: > 10 } => "large-upload",
    { Kind: "upload" } => "small-upload",
    _ => "other",
};
Console.WriteLine(Route(new Event("upload", 12)));
```

**Simple Python example from this file**
```python
def classify(value):
    match value:
        case 0:
            return "zero"
        case int() as n if n > 0:
            return "positive"
        case _:
            return "other"

print(classify(3))
```

**Advanced Python example from this file**
```python
from dataclasses import dataclass

@dataclass
class Event:
    kind: str
    size: int

def route(event: Event) -> str:
    match event:
        case Event(kind="upload", size=size) if size > 10:
            return "large-upload"
        case Event(kind="upload"):
            return "small-upload"
        case _:
            return "other"

print(route(Event("upload", 12)))
```

**Python equivalent**
Python approaches this concept with less ceremony: Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Pattern matching` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Pattern matching`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- positive
- large-upload
