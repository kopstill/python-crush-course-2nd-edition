class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print("Invalid mileage!")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def upgrade_battery(self, battery_size=100):
        print("Upgrade battery...")
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            run_range = 260
        elif self.battery_size == 100:
            run_range = 315
        else:
            run_range = '[unknown]'

        print(f'This car can go about {run_range} miles on a full charge.')


class ElectricCar(Car):
    def __init__(self, make, model, year, run_range=100):
        super().__init__(make, model, year)
        self.battery = Battery(run_range)

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(1)
# my_new_car.read_odometer()
