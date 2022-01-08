guests = ['Turing', 'Einstein', 'Hawking']
print(guests)

canceled_guest = guests.pop(1)
print(f'{canceled_guest} canceled')
print(guests)

new_guest = 'Newton'
guests.append(new_guest)
print(guests)

more_guest_0 = 'Edison'
guests.insert(0, more_guest_0)
print(guests)
more_guest_1 = 'Curie'
guests.insert(2, more_guest_1)
print(guests)
more_guest_2 = 'Tesla'
guests.append(more_guest_2)
print(guests)
print(len(guests))

guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(0)
print(guests)

del guests[0]
del guests[0]
print(guests)
