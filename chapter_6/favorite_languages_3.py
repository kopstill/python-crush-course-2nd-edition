favorite_languages = {
    'jen': ['python', 'c', 'rust'],
    'sarah': ['c', 'java', 'sql'],
    'edward': ['ruby', 'python', 'c++'],
    'phil': ['python', 'javascript', 'shell'],
    'tristan': ["java"]
}
print(favorite_languages)

for name, language in favorite_languages.items():
    if len(language) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for lang in language:
            print(f"\t{lang.title()}")
    else:
        print(f"{name.title()}'s favorite languages is:")
        for lang in language:
            print(f"\t{lang.title()}")
