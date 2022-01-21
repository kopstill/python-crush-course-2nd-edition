class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self):
        print("Fill gas tank")


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


my_tesla = ElectricCar('tesla', 'model s', 2019, 75)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
