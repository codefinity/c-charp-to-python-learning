### 58. `__slots__` as a language feature
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py)

**What C# developers usually expect**
C# developers usually expect object field layout to be explicit and stable.

**C# example**
Simple equivalent:
```csharp
sealed class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
}
Console.WriteLine("has __dict__:False");
```

Advanced equivalent:
```csharp
record Event(int EventId, int Priority);
var e = new Event(101, 2);
Console.WriteLine($"slot dataclass:{e.Priority}");
```

**Simple Python example from this file**
```python
point = Point(2, 4)
print(f"has __dict__:{hasattr(point, '__dict__')}")
```

**Advanced Python example from this file**
```python
event = Event(event_id=101, priority=2)
print(f"slot dataclass:{event.priority}")
```

**Python equivalent**
`__slots__` restricts dynamic attribute creation and can reduce per-instance memory overhead.

**Detailed explanation for C# developers**
Use slots in hot paths with many short-lived objects, but avoid them when dynamic attributes are required.

**Common mistakes for C# developers**
1. Assuming slots make objects immutable.
2. Adding dynamic fields to slotted classes without planning.

**Exercises**
1. Convert one high-volume model to slots and benchmark memory.
2. Decide where slots hurt flexibility in your codebase.

**Expected output**
- has __dict__:False
- slot dataclass:2
