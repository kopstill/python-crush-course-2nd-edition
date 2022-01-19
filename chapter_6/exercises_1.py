people = [
    {"daniel": "123"},
    {"tom": "456"},
    {"david": "789"}
]
for person in people:
    for name, detail in person.items():
        print(f"Name: {name.title()}, Number: {detail}")

print("#################")

pets = [
    {"category": "cat", "master": "tom"},
    {"category": "dog", "master": "lisa"},
    {"category": "rabbit", "master": "linda"}
]
for pet in pets:
    print(f"{pet['master'].title()} got a pet, category is {pet['category']}.")

print("#################")

favorite_places = {
    "tom": ["chengdu", "chongqing", "guangzhou"],
    "daniel": ["shanghai", "beijing", "hangzhou"],
    "michael": ["shenzhen", "changsha", "wuhan"]
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

print("#################")

favorite_numbers = {
    'tom': [11, 6, 21],
    'jack': [3, 23, 14],
    'david': [23, 11, 8],
    'tristan': [7, 14, 32],
    'michael': [16, 21, 31]
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

print("#################")

cities = {
    "guangzhou": {
        "country": "china",
        "population": 30_000_000,
        "fact": "canton"
    },
    "paris": {
        "country": "france",
        "population": 10_000_000,
        "fact": "La Tour Eiffel"
    },
    "liverpool": {
        "country": "england",
        "population": 800_000,
        "fact": "anfield"
    }
}
for name, detail in cities.items():
    print(f"{name.title()}'s detail:")
    for key, value in detail.items():
        if key == 'country' or key == 'fact':
            print(f"\t{key.title()}: {value.title()}")
        else:
            print(f"\t{key.title()}: {value}")
