print('Enter two numbers for add.')
print("Enter 'q' to quit.\n")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Invalid number!\n')
    else:
        print(f'Answer is: {result}\n')
