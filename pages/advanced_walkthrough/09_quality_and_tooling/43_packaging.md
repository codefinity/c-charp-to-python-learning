### 43. Packaging
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var metadata = new Dictionary<string, string>
{
    ["name"] = "csharp-to-python-learning",
    ["entry_point"] = "dotnet run",
};
Console.WriteLine(metadata["name"]);
```

Advanced equivalent:
```csharp
var buildSteps = new[] { "uv sync", "uv run -m pytest", "uv build" };
Console.WriteLine(string.Join(" -> ", buildSteps));
```

**Simple Python example from this file**
```python
metadata = {
    "name": "csharp-to-python-learning",
    "entry_point": "python -m csharp_to_python_learning",
}
print(metadata["name"])
```

**Advanced Python example from this file**
```python
build_steps = ["uv sync", "uv run -m pytest", "uv build"]
print(" -> ".join(build_steps))
```

**Python equivalent**
Python approaches this concept with less ceremony: Packaging turns source code into installable artifacts with metadata and entry points. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Packaging turns source code into installable artifacts with metadata and entry points. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Packaging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Packaging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- csharp-to-python-learning
- uv sync -> uv run -m pytest -> uv build
