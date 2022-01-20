def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


greet_users('abc')  # This is a string
greet_users(['jack', 'tom'])  # This is a list
greet_users({"aaa": "bbb", "ccc": "ddd"})  # This is a dict
greet_users({"eee", "fff", 'ggg'})  # This is a set
