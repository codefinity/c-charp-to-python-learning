### 56. Binary data: `bytes`, `bytearray`, and `memoryview`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py)

**What C# developers usually expect**
C# developers usually work with `byte[]`, `Span<T>`, and buffer slices.

**C# example**
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

**Simple Python example from this file**
```python
payload = b"hello"
print(payload.hex())
```

**Advanced Python example from this file**
```python
buffer = bytearray(b"abcde")
view = memoryview(buffer)
view[1:4] = b"XYZ"
print(buffer.decode("ascii"))
```

**Python equivalent**
Python provides immutable `bytes`, mutable `bytearray`, and zero-copy `memoryview`.

**Detailed explanation for C# developers**
Use `memoryview` for high-throughput transformations where copies are expensive.

**Common mistakes for C# developers**
1. Mutating `bytes` (immutable).
2. Copying buffers when a view is enough.

**Exercises**
1. Parse a binary header with `memoryview`.
2. Benchmark slice-copy vs. slice-view on a larger payload.

**Expected output**
- 68656c6c6f
- aXYZe
