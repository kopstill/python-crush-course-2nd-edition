car_name = input("What car do you want to rent?\n")
print(f"Let me see if I can find you a {car_name.title()}.")

print("------------------")

count = input("How many people are eating?\n")
count = int(count)
if count > 8:
    print("Sorry, there's no table is available.")
else:
    print("Let me find you a free table.")

print("------------------")

number = input("Enter a number and I'll tell you if it is multiples of 10.\n")
number = int(number)
if number % 10 == 0:
    print("Yes, it's multiples of 10.")
else:
    print("No, it's not multiples of 10.")
