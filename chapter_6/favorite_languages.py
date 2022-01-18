favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

sarah_language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {sarah_language}.")

print('#####################')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print('#####################')

for name in favorite_languages.keys():
    print(f'Name: {name.title()}')

print('#####################')

for name in favorite_languages:
    print(f'Name: {name.title()}')

print('#####################')

tom_language = favorite_languages.get('tom', 'tom not assigned')
print(tom_language)

jack_language = favorite_languages.get('jack')
print(jack_language)
