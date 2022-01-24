filename = 'alice.txt'

try:
    with open(filename) as file:
        contents = file.read()
except (FileNotFoundError, IOError, EOFError):
    print("Read file error!")
else:
    print(contents.count('you'))
    print(contents.lower().count('you'))
