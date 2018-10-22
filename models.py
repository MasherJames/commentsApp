from datetime import datetime

class Store:
    users = []
    comments = []

class User:
    user_id = 1
    def __init__(self, username = None , email = None , password = None , role = 'normal'):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.id = User.user_id

        User.user_id += 1

    def get_by_username(self, username):
        for user in Store.users:
            if user.username == username:
                return user

class Comments:
    comment_id = 1
    def __init__(self, message = None, author = None):
        self.message = message
        self.author = author
        self.timestamp = datetime.now().replace(second=0, microsecond=0)
        self.id = Comments.comment_id
