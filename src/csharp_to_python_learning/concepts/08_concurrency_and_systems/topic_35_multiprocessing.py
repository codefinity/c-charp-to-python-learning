"""
# 35. Multiprocessing

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var values = new[] { 1, 2, 3 }.AsParallel().Select(n => n * n).ToArray();
Console.WriteLine($"[{string.Join(", ", values)}]");
```

Advanced equivalent:
```csharp
var queue = new System.Collections.Concurrent.BlockingCollection<int>();
var processLike = Task.Run(() => queue.Add(42));
await processLike;
Console.WriteLine(queue.Take());
```

## Python equivalent
Python approaches this concept with less ceremony: Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from multiprocessing import Pool

def square(n: int) -> int:
    return n * n

if __name__ == "__main__":
    with Pool(2) as pool:
        print(pool.map(square, [1, 2, 3]))
```

## Advanced Python example
```python
from multiprocessing import Process, Queue

def worker(queue: Queue[int]) -> None:
    queue.put(42)

if __name__ == "__main__":
    queue: Queue[int] = Queue()
    process = Process(target=worker, args=(queue,))
    process.start()
    process.join()
    print(queue.get())
```

## Detailed explanation
Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Multiprocessing` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Multiprocessing`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- [1, 4, 9]
- 42
"""

from __future__ import annotations

from multiprocessing import Pool, Process, Queue


def _square(value: int) -> int:
    return value * value


def _publish_answer(queue: Queue[int]) -> None:
    queue.put(42)


def simple_python_example() -> None:
    with Pool(2) as pool:
        print(pool.map(_square, [1, 2, 3]))


def advanced_python_example() -> None:
    queue: Queue[int] = Queue()
    process = Process(target=_publish_answer, args=(queue,))
    process.start()
    process.join()
    print(queue.get())


def main() -> None:
    print("=== 35. Multiprocessing ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
