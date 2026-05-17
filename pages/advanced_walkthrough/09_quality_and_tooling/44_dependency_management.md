### 44. Dependency management
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
Simple equivalent:
```csharp
var dependencies = new[] { "httpx>=0.28", "pydantic>=2.8" };
Console.WriteLine(dependencies.Length);
```

Advanced equivalent:
```csharp
var groups = new Dictionary<string, string[]>
{
    ["runtime"] = new[] { "httpx" },
    ["dev"] = new[] { "pytest", "ruff", "mypy" },
};
Console.WriteLine($"[{string.Join(", ", groups["dev"].OrderBy(x => x))}]");
```

**Simple Python example from this file**
```python
dependencies = ["httpx>=0.28", "pydantic>=2.8"]
print(len(dependencies))
```

**Advanced Python example from this file**
```python
groups = {"runtime": ["httpx"], "dev": ["pytest", "ruff", "mypy"]}
print(sorted(groups["dev"]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Pin dependencies and commit lock files for deterministic builds across machines and CI. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Pin dependencies and commit lock files for deterministic builds across machines and CI. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Dependency management` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Dependency management`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 2
- ['mypy', 'pytest', 'ruff']
