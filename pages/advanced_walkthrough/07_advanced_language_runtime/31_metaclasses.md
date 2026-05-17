### 31. Metaclasses
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
class Service
{
    public static string Version => "1.0";
}
Console.WriteLine(Service.Version);
```

Advanced equivalent:
```csharp
abstract class BasePlugin
{
    public static readonly Dictionary<string, Type> Registry = new();
    protected static void Register<T>() where T : BasePlugin => Registry[typeof(T).Name] = typeof(T);
}
class CsvPlugin : BasePlugin { static CsvPlugin() => Register<CsvPlugin>(); }
_ = typeof(CsvPlugin); // force static ctor
Console.WriteLine($"[{string.Join(", ", BasePlugin.Registry.Keys.OrderBy(x => x))}]");
```

**Simple Python example from this file**
```python
class AddVersion(type):
    def __new__(mcls, name, bases, namespace):
        namespace["version"] = "1.0"
        return super().__new__(mcls, name, bases, namespace)

class Service(metaclass=AddVersion):
    version: str

print(Service.version)
```

**Advanced Python example from this file**
```python
class RegistryMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "BasePlugin":
            mcls.registry[name] = cls
        return cls

class BasePlugin(metaclass=RegistryMeta):
    pass

class CsvPlugin(BasePlugin):
    pass

print(sorted(RegistryMeta.registry))
```

**Python equivalent**
Python approaches this concept with less ceremony: Metaclasses customize class creation and are useful for registries and framework hooks. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Metaclasses customize class creation and are useful for registries and framework hooks. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Metaclasses` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Metaclasses`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 1.0
- ['CsvPlugin']
