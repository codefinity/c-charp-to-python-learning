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
