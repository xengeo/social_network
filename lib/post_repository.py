# File: lib/post_repository.py

from lib.post import Post

class PostRepository:

    def __init__(self) -> None:
        # params: connection
        # returns: nothing
        # side-effects: assigns connection to instance var
        pass
        
    def all(self):
        # Params: None
        # Returns: list containing all posts as Post objects
        # Side-effects: Executes SQL SELECT query via db connection
        pass

    def create(self):
        # Add a new post
        # params: post object
        # returns: None
        # side-effects: executes INSERT SQL query via db connection
        pass

