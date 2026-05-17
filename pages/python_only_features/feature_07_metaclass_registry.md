# 7. Metaclass Registry

## Concept summary
Metaclasses let you customize class creation itself.
They are advanced but powerful for plugin registration, declarative frameworks, and class-level enforcement.

## What C# developers usually expect
In C#, this often requires reflection scans, attributes, or explicit startup registration.
Python metaclasses can register subclasses automatically when classes are defined.

## How this example works
`RegistryMeta` inherits from `type` and overrides `__new__`.
Whenever a class using this metaclass is defined, `__new__` runs.
It stores each concrete plugin class in `RegistryMeta.plugins`, skipping the base `Plugin`.
When `SlackPlugin` is declared, it is automatically added to the registry.
`main()` prints the sorted registry keys.

## Why this matters in production
This pattern supports zero-boilerplate plugin discovery for integrations, command handlers, or serialization adapters.
Frameworks can auto-register implementations without separate wiring code.

## Common mistakes
Using metaclasses too early when simple decorators or explicit registries are enough.
Hiding too much magic, which can make debugging harder for teams unfamiliar with the pattern.
Mixing multiple metaclasses unintentionally can cause class creation conflicts.

## Source
- [feature_07_metaclass_registry.py](../../src/csharp_to_python_learning/python_only_features/feature_07_metaclass_registry.py)

## Exact example from code file
```python
class RegistryMeta(type):
    plugins: dict[str, type] = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "Plugin":
            mcls.plugins[name] = cls
        return cls


class Plugin(metaclass=RegistryMeta):
    pass


class SlackPlugin(Plugin):
    pass


def main() -> None:
    print(sorted(RegistryMeta.plugins))


if __name__ == "__main__":
    main()

```

## Run
```bash
uv run src/csharp_to_python_learning/python_only_features/feature_07_metaclass_registry.py
```

## Expected output
- `['SlackPlugin']`




