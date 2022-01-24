filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

print('---')

with open(filename) as file_object:
    for line in file_object:
        print(line)

print('---')

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

print('---')

for line in lines:
    print(line)
