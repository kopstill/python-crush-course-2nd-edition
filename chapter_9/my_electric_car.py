from car import Car, ElectricCar

print('^^^^^^^^^^^^^^^^^^^^')
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_beetle.read_odometer()

print('^^^^^^^^^^^^^^^^^^^^')
my_electric_car = ElectricCar('benz', 's60', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
my_electric_car.update_odometer(237)
my_electric_car.read_odometer()
