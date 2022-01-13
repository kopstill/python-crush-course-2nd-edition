age = 200

if age < 2:
    print("This is a baby.")
elif 2 <= age < 4:
    print('This is a toddler.')
elif 4 <= age < 13:
    print('This is a child.')
elif 13 <= age < 20:
    print('This is a teenager.')
elif 20 <= age < 65:
    print('This is an adult.')
else:
    print('This is an elder.')
