from lib.post import Post


def test_post_initializes():
    post = Post(1, "bob_title_1", "Bob Contents 1", 5, 1)
    assert post.id == 1
    assert post.title == "bob_title_1"
    assert post.content == "Bob Contents 1"
    assert post.views == 5
    assert post.user_id == 1


def test_post_format():
    post = Post(1, "bob_title_1", "Bob Contents 1", 5, 1)

    assert str(post) == "Post(1, bob_title_1, Bob Contents 1, 5, 1)"


def test_post_equals():
    post1 = Post(1, "bob_title_1", "Bob Contents 1", 5, 1)
    post2 = Post(1, "bob_title_1", "Bob Contents 1", 5, 1)

    assert post1 == post2
