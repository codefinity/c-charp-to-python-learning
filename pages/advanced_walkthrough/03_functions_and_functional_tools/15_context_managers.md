### 15. Context managers
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
sealed class LabelledScope : IDisposable
{
    private readonly string _name;
    public LabelledScope(string name) { _name = name; Console.WriteLine($"enter {name}"); }
    public void Dispose() => Console.WriteLine($"exit {_name}");
}
using (new LabelledScope("demo")) Console.WriteLine("inside");
```

Advanced equivalent:
```csharp
var temp = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());
Directory.CreateDirectory(temp);
var path = Path.Combine(temp, "note.txt");
File.WriteAllText(path, "safe write");
Console.WriteLine(File.ReadAllText(path));
Directory.Delete(temp, recursive: true);
```

**Simple Python example from this file**
```python
from contextlib import contextmanager

@contextmanager
def labelled(name: str):
    print(f"enter {name}")
    try:
        yield
    finally:
        print(f"exit {name}")

with labelled("demo"):
    print("inside")
```

**Advanced Python example from this file**
```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "note.txt"
    path.write_text("safe write", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
```

**Python equivalent**
Python approaches this concept with less ceremony: Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Context managers` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Context managers`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- enter demo
- safe write
