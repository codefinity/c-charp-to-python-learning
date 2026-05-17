# 5. Descriptors

## Concept summary
Descriptors customize attribute access at the class level.
They are the protocol behind `property`, method binding, and many ORM/validation fields.

## What C# developers usually expect
C# properties provide accessor logic per property member.
Python descriptors generalize that idea so reusable access behavior can be attached as class attributes.

## How this example works
`Lowercase` is a descriptor with `__set_name__`, `__get__`, and `__set__`.
When `User` class is created, `__set_name__` records the attribute name (`email`).
Setting `user.email` calls `__set__`, which stores a lowercased value in `user.__dict__`.
Reading `user.email` calls `__get__`, returning the normalized value.

## Why this matters in production
Descriptors are useful for reusable validation, normalization, lazy loading, and auditing logic.
Instead of duplicating setter code in many classes, you centralize behavior in one descriptor.

## Common mistakes
Ignoring per-instance storage and accidentally storing state on the descriptor itself.
Forgetting `__set_name__` or using conflicting attribute names.
Using descriptors where a simple `@property` is sufficient.

## Source
- [feature_05_descriptors.py](../../src/csharp_to_python_learning/python_only_features/feature_05_descriptors.py)

## Exact example from code file
```python
class Lowercase:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value.lower()


class User:
    email = Lowercase()


def main() -> None:
    user = User()
    user.email = "TEAM@EXAMPLE.COM"
    print(user.email)


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_05_descriptors.py
```

## Expected output
- `team@example.com`




