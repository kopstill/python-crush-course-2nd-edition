users = ['admin', 'tom', 'david', 'lily', 'lucy', 'michael']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again.')

print()

users = []

if users:
    print(users)
else:
    print('We need to find some users.')

print()

# current_users = ['tom', 'david', 'duo', 'lucy', 'lilei']
current_users = []
new_users = ['TOM', 'Duo', 'Hanmeimei', 'Emma', 'Ava']

if new_users:
    for new_user in new_users:
        if current_users:
            if new_user.lower() in current_users:
                print(f'{new_user.title()} is taken.')
            else:
                print(f'{new_user.title()} is not taken.')
        else:
            print(f'Current no users, {new_user.title()} is available.')
