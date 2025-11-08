import unittest
from shopping_cart import ShoppingCart
from user import User

class TestUserCartIntegration(unittest.TestCase):
    def setUp(self):
        self.user = User("Connor", 150.0)

    def test_checkout_success(self):
        self.user.cart.add_item("cheese", 2, 5)  
        self.user.cart.add_item("crackers", 3, 2) 
        total = self.user.cart.total_cost()

        spent = self.user.checkout()
        self.assertEqual(spent, total)
        self.assertEqual(self.user.balance, 150 - total)
        self.assertEqual(self.user.cart.items, {})

    def test_insufficient_balance(self):
        self.user.cart.add_item("phone", 500, 1)
        with self.assertRaises(ValueError):
            self.user.checkout()

    def test_multiple_checkouts(self):
        self.user.cart.add_item("cheese", 5, 2)
        self.user.checkout()
        bal1 = self.user.balance
        self.user.cart.add_item("crackers", 2, 3)
        self.user.checkout()
        self.assertLess(self.user.balance, bal1)
        self.assertEqual(self.user.cart.items, {})

if __name__ == "__main__":
    unittest.main()
