import unittest 

from src.drink import Drink

    # def test_drink_has_price(self):
    #         self.assertEqual(3.50, self.drink_1.price)



class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Beer", 3.50, 10)


    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink_1.name)

