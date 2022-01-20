class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of the restaurant is: {self.restaurant_name}')
        print(f'The cuisine type of the restaurant is: {self.cuisine_type}')

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now available!")

    def set_number_served(self, number_served):
        self.number_served = number_served


restaurant = Restaurant("McDonalds", "Eason")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('---')

restaurant = Restaurant("KFC", "Agger")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('---')

restaurant = Restaurant("PizzaHut", "Gerrard")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.set_number_served(1024)
print(restaurant.number_served)
