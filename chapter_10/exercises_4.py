filename = 'why_programming.txt'

while True:
    reason = input('Why you love to program? ')

    if reason == 'q' or reason == 'quit':
        break

    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')
