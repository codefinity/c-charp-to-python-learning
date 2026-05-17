### 41. Mocking
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py)

**What C# developers usually expect**
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

**C# example**
Simple equivalent:
```csharp
var client = new Moq.Mock<IClient>();
client.Setup(c => c.Fetch()).Returns(new Dictionary<string, bool> { ["ok"] = true });
Console.WriteLine(client.Object.Fetch()["ok"]);
```

Advanced equivalent:
```csharp
var sender = new Func<Task<string>>(() => Task.FromResult("sent"));
Console.WriteLine(await sender());
```

**Simple Python example from this file**
```python
from unittest.mock import Mock

client = Mock()
client.fetch.return_value = {"ok": True}
print(client.fetch()["ok"])
```

**Advanced Python example from this file**
```python
import asyncio
from unittest.mock import AsyncMock

async def main_async():
    sender = AsyncMock(return_value="sent")
    print(await sender())

asyncio.run(main_async())
```

**Python equivalent**
Python approaches this concept with less ceremony: Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Mocking` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Mocking`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- sent
