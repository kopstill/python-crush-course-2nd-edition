import unittest
from city_functions import get_city_country_name


class CityCountryNameTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name = get_city_country_name('santiago', 'chile')
        self.assertEqual(city_country_name, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_name = get_city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(city_country_name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
