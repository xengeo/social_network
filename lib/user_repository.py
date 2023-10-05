# File: lib/user_repository.py

from lib.user import User

class UserRepository:
    
    def __init__(self, connection) -> None:
        # params: connection
        # returns: nothing
        # side-effects: assigns connection to instance var
        self._connection = connection

    def all(self):
        # Params: None
        # Returns: list containing all users as User objects
        # Side-effects: Executes SQL SELECT query via db connection
        rows = self._connection.execute('select * from users')
        
        users = []
        for row in rows:
            user = User(row['id'], row['email'], ['username'])
            users.append(user)

        return users

    def next_user_id(self):
        result =  self._connection.execute('select (max(id) + 1) as new_id from users')
        return result[0]['new_id']


    def create(self, user):
        # Add a new user
        # params: user object
        # returns: None
        # side-effects: executes INSERT SQL query via db connection
        self._connection.execute(
            'insert into users (email, username) values (%s, %s)', [user.email, user.username])
        return None