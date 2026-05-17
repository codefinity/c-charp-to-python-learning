"""
# 61. Weak references and finalization patterns

## What C# developers usually expect
C# developers usually expect GC-managed objects with explicit disposal for critical resources.

## C# example
```csharp
var cache = new ConditionalWeakTable<object, Metadata>();
```

## Python equivalent
Python provides `weakref` containers and `weakref.finalize` for non-owning references and cleanup callbacks.

## Simple Python example
```python
cache = weakref.WeakValueDictionary()
cache["item"] = obj
```

## Advanced Python example
```python
finalizer = weakref.finalize(resource, callback)
```

## Detailed explanation
Weak references help avoid cache-induced leaks and can trigger cleanup hooks when objects are collected.

## Common mistakes for C# developers
1. Assuming weak references keep objects alive.
2. Depending on exact GC timing for business logic.

## Exercises
1. Replace a strong-reference cache with `WeakValueDictionary`.
2. Add diagnostics around object lifecycle transitions.

## Expected output
- cache alive:True
- cache alive after gc:False
"""

from __future__ import annotations

import gc
import weakref


class Payload:
    def __init__(self, value: int) -> None:
        self.value = value


def simple_python_example() -> None:
    cache: weakref.WeakValueDictionary[str, Payload] = weakref.WeakValueDictionary()
    item = Payload(5)
    cache["item"] = item
    print(f"cache alive:{'item' in cache}")
    del item
    gc.collect()
    print(f"cache alive after gc:{'item' in cache}")


def advanced_python_example() -> None:
    events: list[str] = []
    payload = Payload(7)
    weakref.finalize(payload, events.append, "finalized")
    del payload
    gc.collect()
    print(f"finalized event:{events == ['finalized']}")


def main() -> None:
    print("=== 61. Weak references and finalization patterns ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
