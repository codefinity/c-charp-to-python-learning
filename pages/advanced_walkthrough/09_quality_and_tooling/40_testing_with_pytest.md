### 40. Testing with pytest
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py)

**What C# developers usually expect**
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

**C# example**
Simple equivalent:
```csharp
static int Add(int a, int b) => a + b;
Console.WriteLine(Add(2, 2) == 4);
```

Advanced equivalent:
```csharp
var cases = new[] { (2, 2, 4), (5, 7, 12) };
var results = cases.Select(c => c.Item1 + c.Item2 == c.Item3);
Console.WriteLine(results.All(x => x));
```

**Simple Python example from this file**
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 2) == 4)
```

**Advanced Python example from this file**
```python
cases = [(2, 2, 4), (5, 7, 12)]
results = [left + right == expected for left, right, expected in cases]
print(all(results))
```

**Python equivalent**
Python approaches this concept with less ceremony: `pytest` favors simple functions and powerful assertions for fast test feedback. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
`pytest` favors simple functions and powerful assertions for fast test feedback. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Testing with pytest` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Testing with pytest`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True
