responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'yes':
        continue
    else:
        print("Stop polling.")
        # polling_active = False
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
