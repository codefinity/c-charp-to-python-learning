"""
# 2. Python execution model

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
Console.WriteLine($"module/assembly: {typeof(Program).Assembly.GetName().Name}");
Console.WriteLine("main block runs only when executed as a program entry point");
```

Advanced equivalent:
```csharp
var source = "value = 40 + 2";
var value = 40 + 2; // equivalent compiled expression
Console.WriteLine($"compiled value: {value}");
```

## Python equivalent
Python approaches this concept with less ceremony: Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
module_name = __name__
print(f"module name: {module_name}")
print("main block runs only when executed as a script")
```

## Advanced Python example
```python
source = "value = 40 + 2\nprint('compiled value:', value)"
code_object = compile(source, "<dynamic>", "exec")
exec(code_object)
```

## Detailed explanation
Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Python execution model` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Python execution model`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- module name:
- compiled value: 42
"""

from __future__ import annotations


def simple_python_example() -> None:
    module_name = __name__
    print(f"module name: {module_name}")
    print("main block runs only when executed as a script")


def advanced_python_example() -> None:
    source = "value = 40 + 2\nprint('compiled value:', value)"
    code_object = compile(source, "<dynamic>", "exec")
    exec(code_object)


def main() -> None:
    print("=== 2. Python execution model ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
