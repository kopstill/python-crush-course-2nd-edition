def get_formatted_name(first_name, last_name, midlle_name=''):
    """返回整洁的姓名。"""
    if midlle_name:
        full_name = f"{first_name} {midlle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', "hendrix")
print(musician)
musician = get_formatted_name('john', 'hooker', "lee")
print(musician)
