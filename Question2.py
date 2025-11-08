class User:
    def __init__(self, username, balance):
        from shopping_cart import ShoppingCart  
        self.username = username
        self.balance = balance
        self.cart = ShoppingCart()

    def checkout(self):
        total = self.cart.total_cost()
        if total > self.balance:
            raise ValueError("Balance Insufficient.")              
        self.balance -= total
        self.cart.clear_cart()
        return total  

