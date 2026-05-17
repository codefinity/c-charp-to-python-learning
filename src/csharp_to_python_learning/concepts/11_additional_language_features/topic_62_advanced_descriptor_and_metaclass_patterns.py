"""
# 62. Advanced descriptor and metaclass patterns

## What C# developers usually expect
C# developers usually expect validation and model registration through attributes, base classes, or DI containers.

## C# example
```csharp
[Required]
public string Name { get; set; } = "";
```

## Python equivalent
Python can enforce field rules with descriptors and auto-register model classes with metaclasses.

## Simple Python example
```python
user.name = "Nikhil"
```

## Advanced Python example
```python
print(Account.__fields__)
print(ModelMeta.registry)
```

## Detailed explanation
Descriptors centralize reusable field behavior; metaclasses automate class-time metadata and registration.

## Common mistakes for C# developers
1. Putting too much business logic in metaclasses.
2. Forgetting that descriptor validation runs at assignment time.

## Exercises
1. Add an integer range descriptor and apply it to two models.
2. Build a mini plugin registry with metaclass-based discovery.

## Expected output
- user:Nikhil
- fields:['name', 'owner']
"""

from __future__ import annotations


class NonEmptyText:
    def __set_name__(self, owner: type[object], name: str) -> None:
        self.private_name = f"_{name}"

    def __get__(self, obj: object, objtype: type[object] | None = None) -> str:
        if obj is None:
            return self.private_name
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("text must not be empty")
        setattr(obj, self.private_name, cleaned)


class ModelMeta(type):
    registry: dict[str, type[object]] = {}

    def __new__(
        mcls,
        name: str,
        bases: tuple[type[object], ...],
        namespace: dict[str, object],
    ) -> type[object]:
        cls = super().__new__(mcls, name, bases, namespace)
        fields = [key for key, value in namespace.items() if isinstance(value, NonEmptyText)]
        cls.__fields__ = fields  # type: ignore[attr-defined]
        if name != "BaseModel":
            mcls.registry[name] = cls
        return cls


class BaseModel(metaclass=ModelMeta):
    __fields__: list[str]


class User(BaseModel):
    name = NonEmptyText()


class Account(BaseModel):
    name = NonEmptyText()
    owner = NonEmptyText()


def simple_python_example() -> None:
    user = User()
    user.name = " Nikhil "
    print(f"user:{user.name}")


def advanced_python_example() -> None:
    print(f"fields:{Account.__fields__}")
    print(f"registry:{sorted(ModelMeta.registry)}")


def main() -> None:
    print("=== 62. Advanced descriptor and metaclass patterns ===")
    print("-- Simple Python example --")
    simple_python_example()
    print("-- Advanced Python example --")
    advanced_python_example()


if __name__ == "__main__":
    main()
