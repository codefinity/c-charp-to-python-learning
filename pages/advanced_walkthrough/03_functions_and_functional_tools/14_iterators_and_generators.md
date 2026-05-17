### 14. Iterators and generators
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
static IEnumerable<int> CountUp(int limit)
{
    for (var current = 0; current < limit; current++) yield return current;
}
Console.WriteLine($"[{string.Join(", ", CountUp(4))}]");
```

Advanced equivalent:
```csharp
IEnumerable<string> Lines() { yield return "alpha"; yield return "beta"; }
IEnumerable<string> Upper(IEnumerable<string> values) => values.Select(v => v.ToUpperInvariant());
Console.WriteLine($"[{string.Join(", ", Upper(Lines()))}]");
```

**Simple Python example from this file**
```python
def count_up(limit: int):
    current = 0
    while current < limit:
        yield current
        current += 1

print(list(count_up(4)))
```

**Advanced Python example from this file**
```python
def lines():
    yield "alpha"
    yield "beta"

def upper(values):
    for value in values:
        yield value.upper()

print(list(upper(lines())))
```

**Python equivalent**
Python approaches this concept with less ceremony: Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Iterators and generators` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Iterators and generators`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [0, 1, 2, 3]
- ['ALPHA', 'BETA']
