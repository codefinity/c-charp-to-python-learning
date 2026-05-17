def describe(value):
    match value:
        case {"kind": "http", "status": status} if status >= 500:
            return "server-error"
        case {"kind": "http", "status": status}:
            return f"http-{status}"
        case _:
            return "unknown"


def main() -> None:
    print(describe({"kind": "http", "status": 503}))


if __name__ == "__main__":
    main()
