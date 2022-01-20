def make_shirt(size='L', word="I love Python"):
    print(f"The shirt's size is: {size}, word is {word}.")


make_shirt("M", "Hello world")
make_shirt()
make_shirt("M")
make_shirt(word='I love Java')
make_shirt(size='S')


def describe_city(city_name='beijing', country_name='china'):
    print(f"{city_name.title()} is in {country_name.title()}.")


describe_city('beijing', 'china')
describe_city("shanghai")
describe_city(city_name="shenzhen")
describe_city(country_name="zhongguo")
describe_city("Reykjavik", 'iceland')
