filename = 'guest_book.txt'

while True:
    guest_name = input("Please enter your name: ")

    if guest_name == 'q' or guest_name == 'quit':
        break
    else:
        print(f'Hello, {guest_name}!')

    with open(filename, 'a') as file_object:
        file_object.write("{}{}".format(guest_name.title(), '\n'))
