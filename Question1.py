import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_and_total(self):
        self.cart.add_item("cheese", 3, 2)     
        self.cart.add_item("crackers", 2.5, 4)  
        self.assertAlmostEqual(self.cart.total_cost(), 16)

    def test_add_existing_item(self):
        self.cart.add_item("cheese", 3, 1)
        self.cart.add_item("cheese", 3, 2)
        self.assertEqual(self.cart.items["cheese"]["quantity"], 3)

    def test_invalid_add(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("cheese", -2, 3)
        with self.assertRaises(ValueError):
            self.cart.add_item("crackers", 2, 0)

    def test_remove_item(self):
        self.cart.add_item("cheese", 4, 1)
        self.cart.remove_item("cheese")
        self.assertNotIn("cheese", self.cart.items)
        with self.assertRaises(KeyError):
            self.cart.remove_item("cheese")

    def test_clear_cart(self):
        self.cart.add_item("crackers", 2, 5)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.items), 0)

if __name__ == "__main__":
    unittest.main()
 
