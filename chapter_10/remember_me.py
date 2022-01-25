import json


def greet_user():
    username = get_stored_username()
    if username:
        message = input(f"Is this your own username, {username}? (yes/no) ")
        if message.lower() == 'yes':
            print(f"Welcome back, {username}!")
        elif message.lower() == 'no':
            get_new_username()
        else:
            print("Wrong input!")
    else:
        get_new_username()


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)

    print(f"We'll remember you when you come back, {username}!")


greet_user()
