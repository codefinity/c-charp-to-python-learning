### 1. Python project setup with uv
Source: [src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py](src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var commands = new[] { "uv init", "uv sync", "uv run src/.../topic_01_python_project_setup_with_uv.py" };
foreach (var command in commands)
{
    Console.WriteLine(command);
}
```

Advanced equivalent:
```csharp
var tooling = new Dictionary<string, string>
{
    ["dependencies"] = "uv add requests",
    ["dev_dependencies"] = "uv add --dev pytest ruff mypy",
    ["lock_refresh"] = "uv sync --upgrade",
};
Console.WriteLine(string.Join(", ", tooling.Select(kv => $"{kv.Key} => {kv.Value}")));
```

**Simple Python example from this file**
```python
commands = [
    "uv init",
    "uv sync",
    "uv run src/csharp_to_python_learning/concepts/.../topic_01_python_project_setup_with_uv.py",
]
for command in commands:
    print(command)
```

**Advanced Python example from this file**
```python
tooling = {
    "dependencies": "uv add requests",
    "dev_dependencies": "uv add --dev pytest ruff mypy",
    "lock_refresh": "uv sync --upgrade",
}
print(", ".join(f"{k} => {v}" for k, v in tooling.items()))
```

**Python equivalent**
Python approaches this concept with less ceremony: Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python project setup with uv` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python project setup with uv`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- uv init
- dependencies => uv add requests
