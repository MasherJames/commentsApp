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
        name = input('Enter your name again: ')
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
                user = User(name, email, pwd_context.encrypt(password))
                Store.users.append(user)
                print('user created successfully!, you can now login')

def login():
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    current_user = User().get_by_username(name)

    while current_user == None:
        print('Incorrect username')
        name = input('Enter your name: ')
    else:
        while not pwd_context.verify(current_user.password, password):
            print('Wrong password, please enter the correct password')
            password = input('Enter your password: ')
        else:
            print('You were successfully logged in {}'.format(name))
            return name

def create_comment():
    author = login()
    message = input('Enter your comment: ')

    while not re.match("^[a-zA-Z0-9]$", message):
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