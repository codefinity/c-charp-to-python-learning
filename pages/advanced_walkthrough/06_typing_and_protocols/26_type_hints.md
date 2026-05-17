### 26. Type hints
Source: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
Simple equivalent:
```csharp
static List<string> Normalize(List<string> names) =>
    names.Select(n => n.Trim()).Select(n => char.ToUpperInvariant(n[0]) + n[1..].ToLowerInvariant()).ToList();
Console.WriteLine($"[{string.Join(", ", Normalize(new List<string> { "  nikhil", "PRIYA " }))}]");
```

Advanced equivalent:
```csharp
var config = new Dictionary<string, object> { ["retries"] = 3, ["timeout"] = 1.5 };
Console.WriteLine(config["retries"]);
```

**Simple Python example from this file**
```python
def normalize(names: list[str]) -> list[str]:
    return [name.strip().title() for name in names]

print(normalize(["  nikhil", "PRIYA "]))
```

**Advanced Python example from this file**
```python
from typing import TypedDict

class Config(TypedDict):
    retries: int
    timeout: float

config: Config = {"retries": 3, "timeout": 1.5}
print(config["retries"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Type hints improve readability and tooling without changing runtime behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Type hints improve readability and tooling without changing runtime behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Type hints` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Type hints`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ['Nikhil', 'Priya']
- 3
