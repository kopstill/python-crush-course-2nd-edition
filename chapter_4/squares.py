squares = []
for value in range(0, 10):
    square = value ** 2
    squares.append(square)

print(squares)

squares = [value ** 2 for value in range(0, 10)]
print(squares)
