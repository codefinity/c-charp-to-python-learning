### 55. Assignment expressions (`:=`)
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py)

**What C# developers usually expect**
C# developers usually declare a variable before condition checks.

**C# example**
Simple equivalent:
```csharp
var items = new[] { "a", "b", "c", "d" };
if ((items.Length) is var size && size > 2) Console.WriteLine($"size:{size}");
```

Advanced equivalent:
```csharp
var raw = new[] { " A ", " ", "B", "", " C" };
var cleaned = raw.Select(item => item.Trim()).Where(item => item.Length > 0).ToList();
Console.WriteLine($"[{string.Join(", ", cleaned)}]");
```

**Simple Python example from this file**
```python
items = ["a", "b", "c", "d"]
if (size := len(items)) > 2:
    print(f"size:{size}")
```

**Advanced Python example from this file**
```python
raw = [" A ", " ", "B", "", " C"]
cleaned = [item for raw_item in raw if (item := raw_item.strip())]
print(cleaned)
```

**Python equivalent**
Python's walrus operator (`:=`) allows assignment inside expressions when it improves clarity.

**Detailed explanation for C# developers**
Use this feature sparingly for readable pipelines, loop conditions, and lightweight parsing.

**Common mistakes for C# developers**
1. Overusing walrus in dense expressions.
2. Hiding important state changes inside nested conditions.

**Exercises**
1. Refactor one parsing loop to use a single walrus assignment.
2. Compare readability with and without walrus in a code review.

**Expected output**
- size:4
- ['A', 'B', 'C']
