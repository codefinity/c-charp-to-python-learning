"""
# 59. Import hooks: custom finders and loaders

## What C# developers usually expect
C# developers usually expect assembly loading to be mostly static at startup.

## C# example
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

## Python equivalent
Python's import system is programmable through `sys.meta_path` with custom finder and loader objects.

## Simple Python example
```python
sys.meta_path.insert(0, finder)
import hooked_module
```

## Advanced Python example
```python
module = importlib.import_module("hooked_config")
print(module.settings)
```

## Detailed explanation
Import hooks are useful for plugin systems, generated modules, and advanced testing seams.

## Common mistakes for C# developers
1. Forgetting to clean up `sys.meta_path` after temporary hooks.
2. Leaving generated modules in `sys.modules` across tests.

## Exercises
1. Build a small plugin loader that resolves modules from a dictionary.
2. Add tests that isolate import hook side effects.

## Expected output
- hooked value:42
- hooked settings:{'mode': 'safe'}
"""

from __future__ import annotations

import importlib
import importlib.abc
import importlib.util
import sys
from collections.abc import Sequence
from types import ModuleType


class DictLoader(importlib.abc.Loader):
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload

    def create_module(self, spec: importlib.machinery.ModuleSpec) -> ModuleType | None:
        return None

    def exec_module(self, module: ModuleType) -> None:
        for key, value in self.payload.items():
            setattr(module, key, value)


class DictFinder(importlib.abc.MetaPathFinder):
    def __init__(self, modules: dict[str, dict[str, object]]) -> None:
        self.modules = modules

    def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None,
        target: ModuleType | None = None,
    ) -> importlib.machinery.ModuleSpec | None:
        if fullname not in self.modules:
            return None
        loader = DictLoader(self.modules[fullname])
        return importlib.util.spec_from_loader(fullname, loader)


def run_with_hook(module_name: str, modules: dict[str, dict[str, object]]) -> ModuleType:
    finder = DictFinder(modules)
    sys.meta_path.insert(0, finder)
    try:
        sys.modules.pop(module_name, None)
        importlib.invalidate_caches()
        return importlib.import_module(module_name)
    finally:
        sys.meta_path.remove(finder)
        sys.modules.pop(module_name, None)


def simple_python_example() -> None:
    module = run_with_hook("hooked_module", {"hooked_module": {"value": 42}})
    print(f"hooked value:{module.value}")


def advanced_python_example() -> None:
    module = run_with_hook("hooked_config", {"hooked_config": {"settings": {"mode": "safe"}}})
    print(f"hooked settings:{module.settings}")


def main() -> None:
    print("=== 59. Import hooks: custom finders and loaders ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
