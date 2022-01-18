favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

tom_language = favorite_languages.get('tom', 'tom not assigned')
print(tom_language)

jack_language = favorite_languages.get('jack')
print(jack_language)
