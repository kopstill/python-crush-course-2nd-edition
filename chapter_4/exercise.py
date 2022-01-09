print([value for value in range(1, 21)])

# big_list = [value for value in range(1, 1_000_000)]
# print(big_list)
# print(min(big_list))
# print(max(big_list))
# print(sum(big_list))

print()

odd_list = range(1, 20, 2)
for value in odd_list:
    print(value)

print()

three_list = range(3, 30, 3)
for value in three_list:
    print(value)

print()

cube_list = [value ** 3 for value in range(1, 10)]
for value in cube_list:
    print(value)

print()

cube_list_1 = [value ** 3 for value in range(1, 10)]
print(cube_list_1)
