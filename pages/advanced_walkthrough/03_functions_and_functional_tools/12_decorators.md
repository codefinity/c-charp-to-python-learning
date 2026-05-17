### 12. Decorators
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
void Run() => Console.WriteLine("work");
Console.WriteLine("[demo] start");
Run();
```

Advanced equivalent:
```csharp
static T Timed<T>(Func<T> action)
{
    var sw = System.Diagnostics.Stopwatch.StartNew();
    var result = action();
    sw.Stop();
    Console.WriteLine($"elapsed={sw.Elapsed.TotalMilliseconds / 1000.0:F6}");
    return result;
}
Console.WriteLine(Timed(() => Enumerable.Range(0, 10_000).Sum()));
```

**Simple Python example from this file**
```python
from functools import wraps

def tagged(tag: str):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{tag}] start")
            return func(*args, **kwargs)

        return wrapper

    return deco

@tagged("demo")
def run():
    print("work")

run()
```

**Advanced Python example from this file**
```python
import time

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"elapsed={time.perf_counter() - start:.6f}")
        return result

    return wrapper

@timed
def compute():
    return sum(range(10_000))

print(compute())
```

**Python equivalent**
Python approaches this concept with less ceremony: Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Decorators` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Decorators`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [demo] start
- elapsed=
