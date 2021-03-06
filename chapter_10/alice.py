filename = 'alice.txt'

try:
    with open(filename, encoding='utf8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The {filename} has about {num_words} words.")
