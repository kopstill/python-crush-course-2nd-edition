rivers = {
    "nile": "egypt",
    "changjiang": "china",
    "amazon": "mexico"
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

print('###################')
for river_name in rivers:
    print(river_name)
print('###################')
for country in rivers.values():
    print(country)
print('###################')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['jen', 'edward']

for name in favorite_languages:
    if name in friends:
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, please taking the poll!")
