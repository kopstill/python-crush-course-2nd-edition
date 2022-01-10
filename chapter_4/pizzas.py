pizzas = ['Pizza Hut', "Domino's Pizza", "Papa John's Pizza"]
for pizza in pizzas:
    print(pizza)
    print(f'I like {pizza} pizza.\n')

print("I really love pizza!\n")

friend_pizzas = pizzas[::]
pizzas.append("Lacesar")
friend_pizzas.append("PizzaMarzano")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print()

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
