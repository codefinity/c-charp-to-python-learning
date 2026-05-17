### 45. Virtual environments
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
Simple equivalent:
```csharp
var hasVirtualEnv = Environment.GetEnvironmentVariable("VIRTUAL_ENV") is not null;
Console.WriteLine(hasVirtualEnv);
```

Advanced equivalent:
```csharp
var venvHint = Environment.GetEnvironmentVariable("VIRTUAL_ENV") is not null ? ".venv" : "no-active-venv";
Console.WriteLine(venvHint);
```

**Simple Python example from this file**
```python
import sys

print(sys.prefix != sys.base_prefix)
```

**Advanced Python example from this file**
```python
import sys

venv_hint = ".venv" if sys.prefix != sys.base_prefix else "no-active-venv"
print(venv_hint)
```

**Python equivalent**
Python approaches this concept with less ceremony: Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Virtual environments` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Virtual environments`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- False
- no-active-venv
