"""
# 56. Binary data: `bytes`, `bytearray`, and `memoryview`

## What C# developers usually expect
C# developers usually work with `byte[]`, `Span<T>`, and buffer slices.

## C# example
Simple equivalent:
```csharp
var payload = System.Text.Encoding.UTF8.GetBytes("hello");
Console.WriteLine(Convert.ToHexString(payload).ToLowerInvariant());
```

Advanced equivalent:
```csharp
var buffer = new byte[] { (byte)'a', (byte)'b', (byte)'c', (byte)'d', (byte)'e' };
var view = buffer.AsSpan();
"XYZ"u8.CopyTo(view[1..4]);
Console.WriteLine(System.Text.Encoding.ASCII.GetString(buffer));
```

## Python equivalent
Python provides immutable `bytes`, mutable `bytearray`, and zero-copy `memoryview`.

## Simple Python example
```python
payload = b"hello"
print(payload.hex())
```

## Advanced Python example
```python
buffer = bytearray(b"abcde")
view = memoryview(buffer)
view[1:4] = b"XYZ"
```

## Detailed explanation
Use `memoryview` for high-throughput transformations where copies are expensive.

## Common mistakes for C# developers
1. Mutating `bytes` (immutable).
2. Copying buffers when a view is enough.

## Exercises
1. Parse a binary header with `memoryview`.
2. Benchmark slice-copy vs. slice-view on a larger payload.

## Expected output
- 68656c6c6f
- aXYZe
"""

from __future__ import annotations


def simple_python_example() -> None:
    payload = b"hello"
    print(payload.hex())


def advanced_python_example() -> None:
    buffer = bytearray(b"abcde")
    view = memoryview(buffer)
    view[1:4] = b"XYZ"
    print(buffer.decode("ascii"))


def main() -> None:
    print("=== 56. Binary data: `bytes`, `bytearray`, and `memoryview` ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
