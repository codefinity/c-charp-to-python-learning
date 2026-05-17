### 4. Primitive types
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
Simple equivalent:
```csharp
decimal amount = 19.99m * 3;
Console.WriteLine($"{amount.GetType().Name} {amount}");
```

Advanced equivalent:
```csharp
var ratio = 1.0 / 3.0 + 1.0 / 6.0;
Console.WriteLine($"fraction: 1/2 as float: {ratio:F1}");
```

**Simple Python example from this file**
```python
from decimal import Decimal

amount = Decimal("19.99") * 3
print(type(amount).__name__, amount)
```

**Advanced Python example from this file**
```python
from fractions import Fraction

ratio = Fraction(1, 3) + Fraction(1, 6)
print("fraction:", ratio, "as float:", float(ratio))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Primitive types` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Primitive types`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Decimal 59.97
- fraction: 1/2 as float: 0.5
