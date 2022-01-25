import json

filename = 'favorite_number.json'
try:
    with open(filename) as file:
        favorite_number = json.load(file)
except FileNotFoundError:
    favorite_number = input("Enter your favorite number: ")
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
else:
    print(f"I know your favorite number! It's: {favorite_number}.")
