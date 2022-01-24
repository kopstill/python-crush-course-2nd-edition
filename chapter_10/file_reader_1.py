with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print('---')

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

print(lines)
