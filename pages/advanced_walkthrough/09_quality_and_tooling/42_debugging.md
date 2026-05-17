### 42. Debugging
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
static double Divide(int a, int b) => a / (double)b;
try { _ = Divide(5, 0); }
catch (DivideByZeroException ex) { Console.WriteLine(ex.GetType().Name); }
```

Advanced equivalent:
```csharp
try { throw new InvalidOperationException("boom"); }
catch (InvalidOperationException ex) { Console.WriteLine(ex.ToString().Split('
').First()); }
```

**Simple Python example from this file**
```python
def divide(a: int, b: int) -> float:
    return a / b

try:
    divide(5, 0)
except ZeroDivisionError as exc:
    print(type(exc).__name__)
```

**Advanced Python example from this file**
```python
import traceback

def fail():
    raise RuntimeError("boom")

try:
    fail()
except RuntimeError:
    text = traceback.format_exc().splitlines()[-1]
    print(text)
```

**Python equivalent**
Python approaches this concept with less ceremony: Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Debugging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Debugging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ZeroDivisionError
- RuntimeError: boom
