import random

from Customer import Customer


class Shipment:

    STATUSES = ('processing', 'shipped', 'delivered')
    counter = 0

    def __init__(self, address):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def change_status_to_next(self) -> bool:
        if self.status == len(Shipment.STATUSES) - 1:
            print('Bad status')
            return False
        self.status += 1
        return True


class Order:

    def __init__(self, customer: Customer, shipment_address: str):
        self.order_num = random.randint(10_000, 1_000_000)
        self.customer = customer
        self.shipment = Shipment(shipment_address)
        self.order_items = []

    def add_item_to_order(self, sku: str, qty: float, price: float):
        self.order_items.append({
            'sku': sku,
            'qty': qty,
            'price': price
        })

    def get_total_price(self):
        total = 0
        for item in self.order_items:
            total += item['price'] * item['qty']
        return total

    def __repr__(self):
        return f"Order number {self.order_num}, total items: " \
               f"{len(self.order_items)}, total: {self.get_total_price()}"