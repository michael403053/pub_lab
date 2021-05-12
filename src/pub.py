

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink_to_stock(self, drink):
        self.drinks.append(drink)

    def customer_buy_drink(self, drink, customer):
        if self.check_age(customer) and customer.drunkness < 60:
            customer.pay_for_drink(drink.price)
            self.update_till(drink.price)
            customer.customer_drunkness(drink)
        
       
    def update_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    


    
        

    
 

    

