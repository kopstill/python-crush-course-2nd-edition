def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name.title(), 'last_name': last_name.title()}
    if age:
        person['age'] = age
    return person


musician = build_person('john', 'wick')
print(musician)
musician = build_person('john', 'wick', age=32)
print(musician)
