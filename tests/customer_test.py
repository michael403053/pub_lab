import unittest 
# from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("George", 10.00, 22, 20)
        self.drink = Drink("voddy coke", 2.50, 10)

    def test_customer_has_name(self):
        self.assertEqual("George", self.customer.name)

    def test_customer_has_money(self):
        self.assertLess(0, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(22, self.customer.age)

    def test_customer_drunkness(self):
        self.customer.customer_drunkness(self.drink)
        self.assertEqual(30, self.customer.drunkness)