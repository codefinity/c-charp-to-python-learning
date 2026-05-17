### 17. Modules and packages
Source: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
Simple equivalent:
```csharp
var payload = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, string>>("{"status":"ok"}")!;
Console.WriteLine(payload["status"]);
```

Advanced equivalent:
```csharp
var mean = new[] { 2.0, 4.0, 8.0 }.Average();
Console.WriteLine(mean);
```

**Simple Python example from this file**
```python
import json

payload = json.loads('{"status":"ok"}')
print(payload["status"])
```

**Advanced Python example from this file**
```python
import importlib

module = importlib.import_module("statistics")
print(module.mean([2, 4, 8]))
```

**Python equivalent**
Python approaches this concept with less ceremony: A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Modules and packages` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Modules and packages`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ok
- 4.666
