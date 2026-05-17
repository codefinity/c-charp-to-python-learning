### 57. Advanced typing: `ParamSpec`, `TypeVarTuple`, `Literal`, `Annotated`, `Self`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py)

**What C# developers usually expect**
C# developers usually expect compile-time generic metadata and fluent APIs with strong type flow.

**C# example**
Simple equivalent:
```csharp
static Func<TIn, TOut> Traced<TIn, TOut>(Func<TIn, TOut> func)
{
    return value => { Console.WriteLine($"traced:{func.Method.Name}"); return func(value); };
}
var add = Traced<int, int>(x => x + 3);
Console.WriteLine(add(2));
```

Advanced equivalent:
```csharp
record Row<T1, T2>(T1 Item1, T2 Item2);
var row = new Row<int, string>(10, "ok");
Console.WriteLine($"row:({row.Item1}, {row.Item2})");
var filters = new List<string>();
filters.Add("status"); filters.Add("region");
Console.WriteLine($"filters:[{string.Join(", ", filters)}]");
Console.WriteLine("safe@443");
```

**Simple Python example from this file**
```python
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))
```

**Advanced Python example from this file**
```python
row = Row[int, str](10, "ok")
print(f"row:{row.values}")
query = Query().where("status").where("region")
print(f"filters:{query.filters}")
print(fetch("safe", 443))
```

**Python equivalent**
Python typing can express callable signatures (`ParamSpec`), variadic generic shapes (`TypeVarTuple`), value-level modes (`Literal`), metadata (`Annotated`), and fluent `Self`.

**Detailed explanation for C# developers**
These hints improve editor accuracy, API contracts, and static checks without changing runtime semantics.

**Common mistakes for C# developers**
1. Expecting type hints to enforce runtime behavior automatically.
2. Ignoring value-level contracts where `Literal` improves safety.

**Exercises**
1. Convert one decorator-heavy helper to use `ParamSpec`.
2. Add `Literal` modes to one public API.

**Expected output**
- traced:add
- row:(10, 'ok')
