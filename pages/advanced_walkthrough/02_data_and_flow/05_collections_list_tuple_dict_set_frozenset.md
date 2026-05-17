### 5. Collections: list, tuple, dict, set, frozenset
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var items = new List<string> { "build", "test", "deploy" };
var mapping = new Dictionary<string, int> { ["build"] = 1, ["test"] = 2 };
var unique = new HashSet<string>(items);
Console.WriteLine($"{items[0]} {mapping["test"]} {unique.Contains("deploy")}");
```

Advanced equivalent:
```csharp
var permissions = new HashSet<string> { "read", "write" };
var profile = ("nikhil", "senior", permissions);
Console.WriteLine($"{profile.Item1} [{string.Join(", ", profile.Item3.OrderBy(x => x))}]");
```

**Simple Python example from this file**
```python
items = ["build", "test", "deploy"]
mapping = {"build": 1, "test": 2}
unique = set(items)
print(items[0], mapping["test"], "deploy" in unique)
```

**Advanced Python example from this file**
```python
permissions = frozenset({"read", "write"})
profile = ("nikhil", "senior", permissions)
print(profile[0], sorted(profile[2]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Collections: list, tuple, dict, set, frozenset` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Collections: list, tuple, dict, set, frozenset`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- build 2 True
- nikhil ['read', 'write']
