# File: lib/post_repository.py

from lib.post import Post


class PostRepository:
    def __init__(self, connection) -> None:
        # params: connection
        # returns: nothing
        # side-effects: assigns connection to instance var
        self._connection = connection

    def all(self):
        # Params: None
        # Returns: list containing all posts as Post objects
        # Side-effects: Executes SQL SELECT query via db connection
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            post = Post(
                row["id"], row["title"], row["content"], row["views"], row["user_id"]
            )
            posts.append(post)

        return posts

    def create(self, post):
        # Add a new post
        # params: post object
        # returns: None
        # side-effects: executes INSERT SQL query via db connection
        self._connection.execute(
            "INSERT INTO posts (title, content, views, user_id) VALUES(%s, %s, %s, %s)",
            [post.title, post.content, post.views, post.user_id],
        )

    def delete(self, id):
        self._connection.execute("DELETE FROM posts WHERE id=%s", [id])
