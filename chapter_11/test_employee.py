import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Albert', 'Einstein', 10000)

    def test_give_default_raise(self):
        annual_salary = self.employee.give_raise()
        self.assertEqual('Albert', self.employee.first_name)
        self.assertEqual('Einstein', self.employee.last_name)
        self.assertEqual(15000, annual_salary)

    def test_give_custom_raise(self):
        annual_salary = self.employee.give_raise(20000)
        self.assertEqual(30000, annual_salary)
