"""
# 41. Mocking

## What C# developers usually expect
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

## C# example
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

## Python equivalent
Python approaches this concept with less ceremony: Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
from unittest.mock import Mock

client = Mock()
client.fetch.return_value = {"ok": True}
print(client.fetch()["ok"])
```

## Advanced Python example
```python
from unittest.mock import AsyncMock
import asyncio

async def main_async():
    sender = AsyncMock(return_value="sent")
    print(await sender())

asyncio.run(main_async())
```

## Detailed explanation
Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `Mocking` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `Mocking`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- True
- sent
"""

from __future__ import annotations


def simple_python_example() -> None:
    from unittest.mock import Mock

    client = Mock()
    client.fetch.return_value = {"ok": True}
    print(client.fetch()["ok"])


def advanced_python_example() -> None:
    import asyncio
    from unittest.mock import AsyncMock

    async def main_async():
        sender = AsyncMock(return_value="sent")
        print(await sender())

    asyncio.run(main_async())


def main() -> None:
    print("=== 41. Mocking ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
