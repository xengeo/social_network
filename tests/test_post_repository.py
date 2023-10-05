# File: test/test_post_repository.py
from lib.post_repository import PostRepository
from lib.post import Post

"""
Test PostRepository#all returns list of a Post objects
reflecting the seed data
"""


def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()

    assert posts == [
        Post(1, "bob_title_1", "Bob Contents 1", 5, 1),
        Post(2, "bob_title_2", "bob Contents 2", 2, 1),
        Post(3, "sarah_title_1", "Sarah Contents 1", 10, 3),
    ]


def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.create(Post(None, "ben_title", "Ben Contents", 100, 1))

    posts = repository.all()
    assert posts == [
        Post(1, "bob_title_1", "Bob Contents 1", 5, 1),
        Post(2, "bob_title_2", "bob Contents 2", 2, 1),
        Post(3, "sarah_title_1", "Sarah Contents 1", 10, 3),
        Post(4, "ben_title", "Ben Contents", 100, 1),
    ]


def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Post(1, "bob_title_1", "Bob Contents 1", 5, 1),
        Post(3, "sarah_title_1", "Sarah Contents 1", 10, 3),
    ]
