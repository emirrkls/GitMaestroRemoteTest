class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, price, quantity):
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] += quantity
            self.inventory[item_id]['price'] = price
        else:
            self.inventory[item_id] = {
                'name': name,
                'price': price,
                'quantity': quantity
            }

    def remove_item(self, item_id, quantity):
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] -= quantity
            if self.inventory[item_id]['quantity'] <= 0:
                del self.inventory[item_id]

    def apply_discount(self, item_id, discount_percentage):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            item['price'] = item['price'] * (1 - discount_percentage / 100)

    def get_total_value(self):
        total = 0.0
        for item in self.inventory.values():
            total += item['price']
        return total
