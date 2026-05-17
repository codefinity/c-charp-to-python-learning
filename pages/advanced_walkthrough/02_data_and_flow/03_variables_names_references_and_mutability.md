### 3. Variables, names, references, and mutability
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var a = new List<int> { 1, 2 };
var b = a;
b.Add(3);
Console.WriteLine($"[{string.Join(", ", a)}] [{string.Join(", ", b)}]");
```

Advanced equivalent:
```csharp
var original = new Dictionary<string, object>
{
    ["region"] = "APAC",
    ["skills"] = new List<string> { "C#", "SQL" },
};
var copyForEdit = new Dictionary<string, object>(original)
{
    ["skills"] = new List<string> { "C#", "SQL", "Python" },
};
Console.WriteLine(original["region"]);
Console.WriteLine(string.Join(", ", (List<string>)copyForEdit["skills"]));
```

**Simple Python example from this file**
```python
a = [1, 2]
b = a
b.append(3)
print(a, b)
```

**Advanced Python example from this file**
```python
original = {"region": "APAC", "skills": ["C#", "SQL"]}
copy_for_edit = {**original, "skills": [*original["skills"], "Python"]}
print(original)
print(copy_for_edit)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Variables, names, references, and mutability` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Variables, names, references, and mutability`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 2, 3] [1, 2, 3]
- {'region': 'APAC', 'skills': ['C#', 'SQL']}
