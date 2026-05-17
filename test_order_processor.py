import unittest
from order_processor import OrderProcessor

class TestOrderProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = OrderProcessor()

    def test_calculate_shipping_express_over_100(self):
        items = [{'name': 'Expensive Item', 'price': 150.0, 'quantity': 1}]
        self.processor.create_order("ORD-001", "CUST-1", items, "express")
        
        shipping = self.processor.calculate_shipping("ORD-001")
        self.assertEqual(shipping, 15.0, "Express shipping should NOT be free, even over $100")

    def test_apply_tax_idempotency(self):
        items = [{'name': 'Item', 'price': 50.0, 'quantity': 1}]
        self.processor.create_order("ORD-002", "CUST-2", items, "standard")
        
        total1 = self.processor.apply_tax_and_finalize("ORD-002")
        total2 = self.processor.apply_tax_and_finalize("ORD-002")
        
        self.assertEqual(total1, 59.0)
        self.assertEqual(total2, 59.0, "Tax should not compound if finalized twice")

    def test_cancel_order_no_discount_key(self):
        items = [{'name': 'Gift', 'price': 10.0, 'quantity': 2}]
        self.processor.create_order("ORD-003", "CUST-3", items, "standard")
        
        try:
            refund = self.processor.cancel_order("ORD-003")
            self.assertEqual(refund, 20.0)
        except KeyError:
            self.fail("cancel_order raised KeyError because 'discount' key was missing.")

if __name__ == '__main__':
    unittest.main()
