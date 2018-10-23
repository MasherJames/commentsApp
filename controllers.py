import re
from passlib.context import CryptContext
from datetime import datetime
from models import Store, User, Comments

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def create_admin():
    admin = User('admin', 'admin@gmail.com', pwd_context.encrypt('adminpass'), 'admin')
    Store.users.append(admin)

def create_moderate():
    moderator = User('moderator', 'moderator@gmail.com', pwd_context.encrypt('moderatorpass'), 'moderator')
    Store.users.append(moderator)

def signUp():
    username = input('Enter your username: ')
    while not re.match("^[a-zA-Z0-9]{4,}$", username):
        print('Invalid username,username should be alphanumeric and min of 6 chars')
        username = input('Enter your username again: ')
    else:
        email = input('Enter your email: ')
        while not re.match("^[^@]+@[^@]+\.[^@]+$", email):
            print('Invalid email')
            email = input('Enter your email again: ')
        else:
            password = input('Enter your password: ')
            while not re.match("^[a-zA-Z0-9]{4,}$", password):
                print('Invalid password, password should be alphanumeric and min of 6 chars')
                password = input('Enter your password again: ')
            else:
                user = User(username, email, pwd_context.encrypt(password))
                Store.users.append(user)
                print('user created successfully!, you can now login')

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    current_user = User().get_by_username(username)

    while current_user == None:
        print('Incorrect username')
        username = input('Enter your username again: ')
    else:
        while not pwd_context.verify(password, current_user.password):
            print('Wrong password, please enter the correct password')
            password = input('Enter your password: ')
        else:
            print('You were successfully logged in {}'.format(username))
            return username

def create_comment():
    author = login()
    message = input('Enter your comment: ')

    while not re.match("^[a-zA-Z0-9 ]{5,}$", message):
        print('Please enter a valid comment.')
        message = input('Enter your comment: ')
    else:
        comment = Comments(message, author)
        Store.comments.append(comment.__dict__)
        print('comment successfully created')

def show_comments():
    print(Store.comments)

if __name__ == '__main__':
    signUp()
    create_comment()
    show_comments()