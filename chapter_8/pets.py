def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n---")


describe_pet("cat", "haha")
describe_pet("dog", "yoyo")
describe_pet(animal_type="rabbit", pet_name="willie")
describe_pet(pet_name="willie", animal_type="rabbit")
describe_pet("okay")
describe_pet(pet_name="okay")
describe_pet('1', '2')
