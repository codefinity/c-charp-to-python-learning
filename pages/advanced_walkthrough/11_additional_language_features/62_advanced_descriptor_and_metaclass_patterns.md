### 62. Advanced descriptor and metaclass patterns
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py)

**What C# developers usually expect**
C# developers usually expect validation and model registration through attributes, base classes, or DI containers.

**C# example**
Simple equivalent:
```csharp
class User
{
    private string _name = "";
    public string Name
    {
        get => _name;
        set => _name = string.IsNullOrWhiteSpace(value) ? throw new ArgumentException("name required") : value.Trim();
    }
}
var user = new User { Name = " Nikhil " };
Console.WriteLine($"user:{user.Name}");
```

Advanced equivalent:
```csharp
var fields = new[] { "name", "owner" };
var registry = new[] { "Account", "User" };
Console.WriteLine($"fields:[{string.Join(", ", fields)}]");
Console.WriteLine($"registry:[{string.Join(", ", registry)}]");
```

**Simple Python example from this file**
```python
user = User()
user.name = " Nikhil "
print(f"user:{user.name}")
```

**Advanced Python example from this file**
```python
print(f"fields:{Account.__fields__}")
print(f"registry:{sorted(ModelMeta.registry)}")
```

**Python equivalent**
Python can enforce field rules with descriptors and auto-register model classes with metaclasses.

**Detailed explanation for C# developers**
Descriptors centralize reusable field behavior; metaclasses automate class-time metadata and registration.

**Common mistakes for C# developers**
1. Putting too much business logic in metaclasses.
2. Forgetting that descriptor validation runs at assignment time.

**Exercises**
1. Add an integer range descriptor and apply it to two models.
2. Build a mini plugin registry with metaclass-based discovery.

**Expected output**
- user:Nikhil
- fields:['name', 'owner']
