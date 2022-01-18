favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages):
    print(f'{name.title()}, thank you for taking the poll.')

print("###############")

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

print("###############")

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
