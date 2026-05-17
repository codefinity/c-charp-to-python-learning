### 20. Inheritance and composition
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "woof"; }
Console.WriteLine(new Dog().Speak());
```

Advanced equivalent:
```csharp
interface ISender { string Send(string message); }
class EmailSender : ISender { public string Send(string message) => $"email:{message}"; }
class Notifier
{
    private readonly ISender _sender;
    public Notifier(ISender sender) => _sender = sender;
    public string Notify(string message) => _sender.Send(message);
}
Console.WriteLine(new Notifier(new EmailSender()).Notify("deployed"));
```

**Simple Python example from this file**
```python
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

print(Dog().speak())
```

**Advanced Python example from this file**
```python
class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"

class Notifier:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)

print(Notifier(EmailSender()).notify("deployed"))
```

**Python equivalent**
Python approaches this concept with less ceremony: Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Inheritance and composition` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Inheritance and composition`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- woof
- email:deployed
