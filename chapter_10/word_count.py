def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # pass
    else:
        words_count = len(contents.split())
        print(f"The file {filename} has about {words_count} words.")


filename = 'alice.txt'
count_words(filename)

print('---')

filenames = ['alicex.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
