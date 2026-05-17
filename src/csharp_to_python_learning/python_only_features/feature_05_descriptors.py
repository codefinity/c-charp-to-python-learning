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
