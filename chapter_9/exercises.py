from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        super().__init__(restaurant_name, cuisine_type)
        if flavors is None:
            flavors = ['strawberry', 'apple', 'pear']
        self.flavors = flavors

    def get_flavors(self):
        return self.flavors


print('******************')
ice_cream_stand = IceCreamStand('PizzaHut', 'Michael', ['test'])
ice_cream_stand.describe_restaurant()
print(ice_cream_stand.get_flavors())
