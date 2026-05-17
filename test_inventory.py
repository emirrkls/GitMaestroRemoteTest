import unittest
from inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()
        self.manager.add_item("ITEM1", "Laptop", 1000.0, 5)
        self.manager.add_item("ITEM2", "Mouse", 50.0, 10)

    def test_add_existing_item(self):
        self.manager.add_item("ITEM1", "Laptop", 1000.0, 3)
        self.assertEqual(self.manager.inventory["ITEM1"]['quantity'], 8)

    def test_apply_discount(self):
        self.manager.apply_discount("ITEM2", 10)
        self.assertEqual(self.manager.inventory["ITEM2"]['price'], 45.0)

    def test_get_total_value(self):
        self.assertEqual(self.manager.get_total_value(), 5500.0)

if __name__ == '__main__':
    unittest.main()
