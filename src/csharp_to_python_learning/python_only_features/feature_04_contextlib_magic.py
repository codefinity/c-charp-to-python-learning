from contextlib import contextmanager


@contextmanager
def banner(label: str):
    print(f"start:{label}")
    try:
        yield
    finally:
        print(f"end:{label}")


def main() -> None:
    with banner("deploy"):
        print("inside")


if __name__ == "__main__":
    main()
