class Customer:
    def __init__(self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = float(wallet)
        self.age = age
        self.drunkness = int(drunkness)

    def pay_for_drink(self, price):
        self.wallet -= price

    def customer_drunkness(self, drink):
        self.drunkness += drink.alcohol_level

    def customer_rejuvination(self, food):
        self.drunkness -= food.rejuvination_level

    




