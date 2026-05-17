"""
# 38. JSON, CSV, TOML

## What C# developers usually expect
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

## C# example
Simple equivalent:
```csharp
var payload = new Dictionary<string, object> { ["name"] = "nikhil", ["years"] = 9 };
var text = System.Text.Json.JsonSerializer.Serialize(payload);
var roundTrip = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(text)!;
Console.WriteLine(roundTrip["name"]);
```

Advanced equivalent:
```csharp
var csv = "name,score
A,90
".Split('
', StringSplitOptions.RemoveEmptyEntries);
var score = csv[1].Split(',')[1];
var tomlText = "tool = { name = 'uv' }"; // parse with a TOML lib in production
Console.WriteLine($"{score} uv");
```

## Python equivalent
Python approaches this concept with less ceremony: Python's standard library handles core data formats without external dependencies. You still keep production discipline through tests, typing, and tooling.

## Simple Python example
```python
import json
payload = {"name": "nikhil", "years": 9}
text = json.dumps(payload)
print(json.loads(text)["name"])
```

## Advanced Python example
```python
import csv
import io
import tomllib

buffer = io.StringIO("name,score\nA,90\n")
rows = list(csv.DictReader(buffer))
parsed = tomllib.loads("tool = { name = 'uv' }")
print(rows[0]["score"], parsed["tool"]["name"])
```

## Detailed explanation
Python's standard library handles core data formats without external dependencies. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

## Common mistakes for C# developers
1. Assuming C# defaults apply directly in `JSON, CSV, TOML` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

## Exercises
1. Rewrite one recent C# snippet in Python using this concept: `JSON, CSV, TOML`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

## Expected output
- nikhil
- 90 uv
"""

from __future__ import annotations


def simple_python_example() -> None:
    import json

    payload = {"name": "nikhil", "years": 9}
    text = json.dumps(payload)
    print(json.loads(text)["name"])


def advanced_python_example() -> None:
    import csv
    import io
    import tomllib

    buffer = io.StringIO("name,score\nA,90\n")
    rows = list(csv.DictReader(buffer))
    parsed = tomllib.loads("tool = { name = 'uv' }")
    print(rows[0]["score"], parsed["tool"]["name"])


def main() -> None:
    print("=== 38. JSON, CSV, TOML ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
