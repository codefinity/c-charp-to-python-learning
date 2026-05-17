### 19. Object-oriented programming
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
class Account
{
    public string Owner { get; }
    public int Balance { get; private set; }
    public Account(string owner) => Owner = owner;
    public void Deposit(int amount) => Balance += amount;
}
var a = new Account("Nikhil"); a.Deposit(50); Console.WriteLine($"{a.Owner} {a.Balance}");
```

Advanced equivalent:
```csharp
record TaxedAmount(double Net, double TaxRate)
{
    public double Gross => Net * (1 + TaxRate);
}
Console.WriteLine(Math.Round(new TaxedAmount(100, 0.18).Gross, 2));
```

**Simple Python example from this file**
```python
class Account:
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

a = Account("Nikhil")
a.deposit(50)
print(a.owner, a.balance)
```

**Advanced Python example from this file**
```python
from dataclasses import dataclass

@dataclass
class TaxedAmount:
    net: float
    tax_rate: float

    @property
    def gross(self) -> float:
        return self.net * (1 + self.tax_rate)

print(round(TaxedAmount(100, 0.18).gross, 2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Object-oriented programming` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Object-oriented programming`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Nikhil 50
- 118.0
