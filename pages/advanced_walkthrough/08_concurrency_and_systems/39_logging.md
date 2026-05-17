### 39. Logging
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
Simple equivalent:
```csharp
Console.WriteLine("INFO service started");
```

Advanced equivalent:
```csharp
Console.WriteLine("billing WARNING quota low");
```

**Simple Python example from this file**
```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logging.info("service started")
```

**Advanced Python example from this file**
```python
import logging

logger = logging.getLogger("billing")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.WARNING)
logger.warning("quota low")
```

**Python equivalent**
Python approaches this concept with less ceremony: Structured, leveled logging is the production replacement for `print` debugging. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Structured, leveled logging is the production replacement for `print` debugging. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Logging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Logging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- INFO service started
- billing WARNING quota low
