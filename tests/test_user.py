# File: tests/test_user.py

from lib.user import User

"""
When we initialised a User
we can get our attributes back
"""
def test_user_initialisation():
    new_user = User(6, 'xenia@test.com', 'xenia')

    assert new_user.id == 6
    assert new_user.email == 'xenia@test.com'
    assert new_user.username == 'xenia'