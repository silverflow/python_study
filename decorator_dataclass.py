from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    password: str
    gender: str
    admin: bool = False


if __name__ == "__main__":
    user1 = User(id=1, name="first member", password="somepassword", gender="man")
    print(user1)
    user2 = User(
        id=2, name="second member", password="somepass", gender="woman", admin=True
    )
    print(user2)
    print(user1 == user2)

