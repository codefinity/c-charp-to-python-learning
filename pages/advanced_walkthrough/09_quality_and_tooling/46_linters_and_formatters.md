### 46. Linters and formatters
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
Console.WriteLine("use: uv run ruff check .");
Console.WriteLine("use: uv run ruff format .");
```

Advanced equivalent:
```csharp
var qualityGate = new Dictionary<string, string>
{
    ["lint"] = "ruff check",
    ["format"] = "ruff format",
    ["types"] = "mypy src",
};
Console.WriteLine(string.Join(" | ", qualityGate.Select(kv => $"{kv.Key}:{kv.Value}")));
```

**Simple Python example from this file**
```python
print("use: uv run ruff check .")
print("use: uv run ruff format .")
```

**Advanced Python example from this file**
```python
quality_gate = {"lint": "ruff check", "format": "ruff format", "types": "mypy src"}
print(" | ".join(f"{k}:{v}" for k, v in quality_gate.items()))
```

**Python equivalent**
Python approaches this concept with less ceremony: Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Linters and formatters` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Linters and formatters`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- use: uv run ruff check .
- lint:ruff check
