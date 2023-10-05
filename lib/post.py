# File: lib/post.py


class Post:
    def __init__(self, id, title, content, views, user_id) -> None:
        # Params: id, title, content, views
        # Return: Nothing
        # Side-effects: Assign args to instances vars
        self.id = id
        self.title = title
        self.content = content
        self.views = views
        self.user_id = user_id

    def __eq__(self, other: object) -> bool:
        # Define equality between two objects with identical values
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        # Format object nicely
        return f"Post({self.id}, {self.title}, {self.content}, {self.views}, {self.user_id})"
