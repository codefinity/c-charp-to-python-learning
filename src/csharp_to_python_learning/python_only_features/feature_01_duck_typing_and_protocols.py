from typing import Protocol


class Writer(Protocol):
    def write(self, text: str) -> str: ...


class ConsoleWriter:
    def write(self, text: str) -> str:
        return text.upper()


def publish(writer: Writer) -> str:
    return writer.write("pythonic")


def main() -> None:
    print(publish(ConsoleWriter()))


if __name__ == "__main__":
    main()
