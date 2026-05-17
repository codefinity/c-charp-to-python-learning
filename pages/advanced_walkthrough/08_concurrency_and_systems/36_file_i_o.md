### 36. File I/O
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var path = Path.Combine(Path.GetTempPath(), "sample.txt");
File.WriteAllText(path, "hello");
Console.WriteLine(File.ReadAllText(path));
```

Advanced equivalent:
```csharp
var path = Path.Combine(Path.GetTempPath(), "data.log");
File.WriteAllLines(path, Enumerable.Range(0, 3).Select(i => $"line-{i}"));
Console.WriteLine(File.ReadAllLines(path).Last());
```

**Simple Python example from this file**
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "sample.txt"
    path.write_text("hello", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
```

**Advanced Python example from this file**
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.log"
    with path.open("w", encoding="utf-8") as file:
        for index in range(3):
            file.write(f"line-{index}\n")
    print(path.read_text(encoding="utf-8").strip().splitlines()[-1])
```

**Python equivalent**
Python approaches this concept with less ceremony: Prefer explicit encodings and context managers for reliable file handling in production. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Prefer explicit encodings and context managers for reliable file handling in production. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `File I/O` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `File I/O`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- hello
- line-2
