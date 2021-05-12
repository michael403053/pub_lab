import unittest 
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("George", 10.00, 22, 20)
        self.drink_1 = Drink("Beer", 3.50, 10)
        self.drink_2 = Drink("Gin", 5.50, 20)
        self.drink_3 = Drink("Wine", 4.00, 15)
        self.food = Food("Burger", 5, 5)
        self.pub.add_drink_to_stock(self.drink_1)
        self.pub.add_drink_to_stock(self.drink_2)
        self.pub.add_drink_to_stock(self.drink_3)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name) 
        

    def test_stock_list(self):   
        self.assertEqual(3, len(self.pub.drinks))

    def test_customer_buy_drink(self):
        self.pub.customer_buy_drink(self.drink_1, self.customer)
        self.assertEqual(6.50, self.customer.wallet)
        self.assertEqual(103.50, self.pub.till)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))
       


    

