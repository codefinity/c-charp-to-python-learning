"""
# 34. Threading

## What C# developers usually expect
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Threading works well for blocking I/O integration, protected with locks for shared mutable state. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import threading

counter = 0
lock = threading.Lock()

def inc():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=inc)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)
```

## Advanced Python example
```python
from concurrent.futures import ThreadPoolExecutor

def upper(text: str) -> str:
    return text.upper()

with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(upper, ["a", "b", "c"])))
```

## Detailed explanation
Threading works well for blocking I/O integration, protected with locks for shared mutable state. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Threading` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Threading`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- 2000
- ['A', 'B', 'C']
"""

from __future__ import annotations


def simple_python_example() -> None:
    import threading

    counter = {"value": 0}
    lock = threading.Lock()

    def inc() -> None:
        for _ in range(1000):
            with lock:
                counter["value"] += 1

    t1 = threading.Thread(target=inc)
    t2 = threading.Thread(target=inc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter["value"])


def advanced_python_example() -> None:
    from concurrent.futures import ThreadPoolExecutor

    def upper(text: str) -> str:
        return text.upper()

    with ThreadPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(upper, ["a", "b", "c"])))


def main() -> None:
    print("=== 34. Threading ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
