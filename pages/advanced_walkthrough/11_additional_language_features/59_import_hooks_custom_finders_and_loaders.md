### 59. Import hooks: custom finders and loaders
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py)

**What C# developers usually expect**
C# developers usually expect assembly loading to be mostly static at startup.

**C# example**
Simple equivalent:
```csharp
var value = 42;
Console.WriteLine($"hooked value:{value}");
```

Advanced equivalent:
```csharp
var settings = new Dictionary<string, string> { ["mode"] = "safe" };
Console.WriteLine("hooked settings:{'mode': 'safe'}");
```

**Simple Python example from this file**
```python
module = run_with_hook("hooked_module", {"hooked_module": {"value": 42}})
print(f"hooked value:{module.value}")
```

**Advanced Python example from this file**
```python
module = run_with_hook("hooked_config", {"hooked_config": {"settings": {"mode": "safe"}}})
print(f"hooked settings:{module.settings}")
```

**Python equivalent**
Python's import system is programmable through `sys.meta_path` with custom finder and loader objects.

**Detailed explanation for C# developers**
Import hooks are useful for plugin systems, generated modules, and advanced testing seams.

**Common mistakes for C# developers**
1. Forgetting to clean up `sys.meta_path` after temporary hooks.
2. Leaving generated modules in `sys.modules` across tests.

**Exercises**
1. Build a small plugin loader that resolves modules from a dictionary.
2. Add tests that isolate import hook side effects.

**Expected output**
- hooked value:42
- hooked settings:{'mode': 'safe'}
