filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    pi_content = file_object.read()

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_content:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi!')
