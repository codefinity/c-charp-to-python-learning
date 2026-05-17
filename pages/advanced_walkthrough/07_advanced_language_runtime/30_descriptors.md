### 30. Descriptors
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
class Order
{
    private int _quantity;
    public int Quantity
    {
        get => _quantity;
        set
        {
            if (value <= 0) throw new ArgumentOutOfRangeException(nameof(value));
            _quantity = value;
        }
    }
}
var o = new Order { Quantity = 5 };
Console.WriteLine(o.Quantity);
```

Advanced equivalent:
```csharp
class Profile
{
    private string _level = "";
    public string Level
    {
        get { Console.WriteLine($"read level={_level}"); return _level; }
        set => _level = value;
    }
}
var p = new Profile { Level = "senior" };
Console.WriteLine(p.Level);
```

**Simple Python example from this file**
```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private_name, value)

class Order:
    quantity = Positive()

o = Order()
o.quantity = 5
print(o.quantity)
```

**Advanced Python example from this file**
```python
class Tracked:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        value = obj.__dict__[self.name]
        print(f"read {self.name}={value}")
        return value

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class Profile:
    level = Tracked()

p = Profile()
p.level = "senior"
print(p.level)
```

**Python equivalent**
Python approaches this concept with less ceremony: Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Descriptors` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Descriptors`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 5
- read level=senior
