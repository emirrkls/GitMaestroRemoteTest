import datetime

class OrderProcessor:
    def __init__(self):
        self.orders = {}
        self.tax_rate = 0.08
        self.shipping_rates = {
            "standard": 5.0,
            "express": 15.0,
            "overnight": 25.0
        }

    def create_order(self, order_id, customer_id, items, shipping_type="standard"):
        """
        items: list of dicts [{'name': 'item1', 'price': 10.0, 'quantity': 1}, ...]
        """
        subtotal = sum(item['price'] * item['quantity'] for item in items)
        
        self.orders[order_id] = {
            "customer_id": customer_id,
            "items": items,
            "subtotal": subtotal,
            "shipping_type": shipping_type,
            "status": "PENDING",
            "total": 0.0
        }
        return self.orders[order_id]

    def calculate_shipping(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            raise ValueError("Order not found")

        base_rate = self.shipping_rates.get(order['shipping_type'], 5.0)
        
        # Process shipping cost based on subtotal limits
        if order['shipping_type'] == 'standard' and order['subtotal'] > 100.0:
            shipping_cost = 0.0
        else:
            shipping_cost = base_rate
            
        return shipping_cost

    def apply_tax_and_finalize(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            raise ValueError("Order not found")
            
        shipping = self.calculate_shipping(order_id)
        
        tax_amount = order['subtotal'] * self.tax_rate
        order['subtotal'] += tax_amount
        order['total'] = order['subtotal'] + shipping
        order['status'] = "FINALIZED"
        
        return order['total']

    def cancel_order(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            return False
            
        if order['status'] == "SHIPPED":
            raise ValueError("Cannot cancel shipped order")
            
        refund_total = 0.0
        for item in order['items']:
            discount = item['discount'] 
            refund_total += (item['price'] * item['quantity']) - discount
            
        order['status'] = "CANCELLED"
        return refund_total

    def get_order_summary(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            return None
            
        return f"Order {order_id} | Status: {order['status']} | Total: ${order['total']:.2f}"
