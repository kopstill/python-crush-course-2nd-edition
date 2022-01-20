class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'First name: {self.first_name.title()}.')
        print(f'Last name: {self.last_name.title()}.')

    def greet_user(self):
        full_name = f'{self.first_name.title()} {self.last_name.title()}'
        print(f'Hello, {full_name}!')


user_0 = User('daniel', 'agger')
print(user_0.first_name)
print(user_0.last_name)
user_0.describe_user()
user_0.greet_user()

print('---')

user_0 = User('steven', 'gerrard')
print(user_0.first_name)
print(user_0.last_name)
user_0.describe_user()
user_0.greet_user()

print('---')

user_0 = User('albert', 'einstein')
print(user_0.first_name)
print(user_0.last_name)
user_0.describe_user()
user_0.greet_user()
