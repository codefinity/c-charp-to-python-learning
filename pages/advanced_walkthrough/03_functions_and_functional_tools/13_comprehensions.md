### 13. Comprehensions
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
var numbers = new[] { 1, 2, 3, 4, 5 };
var squares = numbers.Where(n => n % 2 == 1).Select(n => n * n);
Console.WriteLine($"[{string.Join(", ", squares)}]");
```

Advanced equivalent:
```csharp
var matrix = new[] { new[] { 1, 2 }, new[] { 3, 4 }, new[] { 5, 6 } };
var flat = matrix.SelectMany(row => row).ToList();
var lookup = flat.ToDictionary(v => v, v => v * v);
Console.WriteLine($"[{string.Join(", ", flat)}] {lookup[6]}");
```

**Simple Python example from this file**
```python
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers if n % 2 == 1]
print(squares)
```

**Advanced Python example from this file**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [cell for row in matrix for cell in row]
lookup = {value: value * value for value in flat}
print(flat, lookup[6])
```

**Python equivalent**
Python approaches this concept with less ceremony: Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Comprehensions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Comprehensions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 9, 25]
- [1, 2, 3, 4, 5, 6] 36
