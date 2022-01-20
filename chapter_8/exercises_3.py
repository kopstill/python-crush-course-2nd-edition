def make_sandwich(*toppings):
    print(toppings)


make_sandwich('pepperoni')
make_sandwich('pepperoni', 'green pepper')
make_sandwich('pepperoni', 'green pepper', 'extra cheese')


def make_car(manufacturer, model, **car):
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car


new_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(new_car)
