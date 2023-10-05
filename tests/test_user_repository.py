from lib.user_repository import UserRepository
from lib.user import User

"""
Test when we run UserRepository#all
we get a list of all users as User objects
"""
def test_all_returns_all_users(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1, 'bobtest@test.com', 'bob'),
        User(2, 'fredtest@test.com', 'fred'),
        User(3, 'sarahtest@test.com', 'sarah'),
        User(4, 'mariatest@test.com', 'maria')
    ]


"""
Test that we can retrieve the next available user_id using
UserRepository#next_user_id returns max id + 1 (integer)
"""
def test_get_max_user_id(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)

    max_id = repository.next_user_id()
    assert max_id == 5

"""
Test that when we run UserRepository#create
we can add a new user to the users PostgreSQL database
"""
def test_create_inserts_new_user(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)

    next_id = repository.next_user_id()
    new_user = User(next_id, 'me@test.com', 'my_username')
    repository.create(new_user)

    all_users = repository.all()
    assert all_users == [
        User(1, 'bobtest@test.com', 'bob'),
        User(2, 'fredtest@test.com', 'fred'),
        User(3, 'sarahtest@test.com', 'sarah'),
        User(4, 'mariatest@test.com', 'maria'),
        User(5, 'me@test.com', 'my_username')
    ]