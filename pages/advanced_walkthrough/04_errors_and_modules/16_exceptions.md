### 16. Exceptions
Source: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
try
{
    _ = int.Parse("not-a-number");
}
catch (FormatException ex)
{
    Console.WriteLine(ex.GetType().Name);
}
finally
{
    Console.WriteLine("cleanup");
}
```

Advanced equivalent:
```csharp
sealed class DomainError : Exception
{
    public DomainError(string message, Exception inner) : base(message, inner) { }
}
static int ParsePort(string raw)
{
    try { return int.Parse(raw); }
    catch (FormatException ex) { throw new DomainError("invalid port", ex); }
}
try { _ = ParsePort("abc"); } catch (DomainError ex) { Console.WriteLine(ex.Message); }
```

**Simple Python example from this file**
```python
try:
    int("not-a-number")
except ValueError as exc:
    print(type(exc).__name__)
finally:
    print("cleanup")
```

**Advanced Python example from this file**
```python
class DomainError(RuntimeError):
    pass

def parse_port(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as exc:
        raise DomainError("invalid port") from exc
    return value

try:
    parse_port("abc")
except DomainError as exc:
    print(exc)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Exceptions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Exceptions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ValueError
- invalid port
