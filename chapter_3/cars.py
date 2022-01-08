cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print(sorted(cars, reverse=True))
print('\nHere is the original list again:')
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print()
print(cars)
print(len(cars))
