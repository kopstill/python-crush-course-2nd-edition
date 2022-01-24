filename = 'cats.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print('File not found')
else:
    print(contents)

print('---')

filename = 'dogs.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    # print('File not found')
    pass
else:
    print(contents)
