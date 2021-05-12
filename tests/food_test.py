import unittest



class TestFood(unittest.TestCase):



    def setUp(self):
        self.food = Food("Burger", 5, 5)
        self.customer = Customer("George", 10.00, 22, 20)

    def test_has_food(self):
        self.assertEqual("Burger", self.food.name)

    def test_customer_rejuvination(self):
        self.customer.customer_rejuvination(self.food)
        self.assertEqual(15, self.customer.drunkness)
