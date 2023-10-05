# File: lib/user.py

class User:

    def __init__(self, user_id, email, username) -> None:
        self.id = user_id
        self.email = email
        self.username = username

    def __eq__(self, other: object) -> bool:
        return self.__doc__ == other.__doc__

    def __repr__(self) -> str:
        return f"User({self.id}, {self.email}, {self.username})"