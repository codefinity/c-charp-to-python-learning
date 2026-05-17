def numbers():
    yield from range(5)


def pipeline():
    return (value * value for value in numbers() if value % 2 == 0)


def main() -> None:
    print(list(pipeline()))


if __name__ == "__main__":
    main()
