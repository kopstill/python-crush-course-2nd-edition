# from car import Car, ElectricCar
# import car
from car import *

print("----------------")
my_new_car = Car('tank', '300', 2021)
full_name = my_new_car.get_descriptive_name()
print(full_name)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print()

my_electric_car = ElectricCar('tesla', 'model s', 2020)
print(my_electric_car.get_descriptive_name())
