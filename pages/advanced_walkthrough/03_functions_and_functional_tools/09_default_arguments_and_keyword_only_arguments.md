### 9. Default arguments and keyword-only arguments
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
static string Greet(string name, bool excited = false) => $"Hello {name}{(excited ? "!" : ".")}";
Console.WriteLine(Greet("Nikhil", excited: true));
```

Advanced equivalent:
```csharp
static List<int> AppendItem(int value, List<int>? bucket = null)
{
    bucket ??= new List<int>();
    bucket.Add(value);
    return bucket;
}
Console.WriteLine($"[{string.Join(", ", AppendItem(1))}] [{string.Join(", ", AppendItem(2))}]");
```

**Simple Python example from this file**
```python
def greet(name: str, *, excited: bool = False) -> str:
    return f"Hello {name}{'!' if excited else '.'}"

print(greet("Nikhil", excited=True))
```

**Advanced Python example from this file**
```python
def append_item(value: int, bucket: list[int] | None = None) -> list[int]:
    bucket = bucket or []
    bucket.append(value)
    return bucket

print(append_item(1), append_item(2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Keyword-only arguments let you model explicit APIs like named optional parameters in C#. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Keyword-only arguments let you model explicit APIs like named optional parameters in C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Default arguments and keyword-only arguments` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Default arguments and keyword-only arguments`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Hello Nikhil!
- [1] [2]
