from Customer import Customer
from store_lesson.orders import Order


class Product:
    def __init__(self, sku: str, category: str, brand: str,
                 qty: float, price: float,
                 model: str = None,
                 warranty_months: int = None):

        self.sku = sku
        self.category = category
        self.brand = brand
        self.model = model
        self.warranty_months = warranty_months
        self.price = price
        self.qty = qty

    def update_qty(self, diff: float):
        if diff + self.qty < 0:
            # error
            return None
        self.qty += diff

    def update_price(self, new_price):
        if new_price <= 0:
            # error
            return None
        self.price = new_price

    def __str__(self):
        return f"<Product>: Brand: {self.brand} Model: {self.model} SKU: {self.sku}"

    def __repr__(self):
        return f"<Product>: Brand: {self.brand}"

    def __eq__(self, other):
        return self.sku == other.sku


class Store:

    def __init__(self, store_name):
        self.store_name = store_name

        # id to customer
        self.customers: dict[str, Customer] = {}

        # sku to product
        self.inventory: dict[str, Product] = {}

        # order_num to order
        self.orders: dict[str, Order] = {}

    def display_customers(self):
        print(self.customers)

    def add_customer(self, customer_id, name, address, phone, email=None):
        print(f"Adding customer {name}")
        new_customer = Customer(customer_id, name, address, phone, email)
        self.customers[customer_id] = new_customer

    # def add_customer2(self, customer: Customer):
    #     self.customers[customer.customer_id] = customer

    def add_product_to_inventory(self, sku: str, category: str, brand: str,
                                 qty: float, price: float,
                                 model: str = None,
                                 warranty_months: int = None):
        print(f"Adding product {brand}")
        new_product = Product(sku, category, brand,
                              qty, price, model, warranty_months)
        self.inventory[sku] = new_product

    def place_order(self, customer_id:str, address: str, items_dict: dict):

        # check customer exists
        if customer_id not in self.customers:
            return False

        # check inventory
        for item_sku, qty in items_dict.items():
            if item_sku not in self.inventory and \
                    self.inventory[item_sku].qty - qty < 0:
                return False

        # create order (sku, qty, price)
        order = Order(self.customers[customer_id], address)
        self.orders[order.order_num] = order
        for item_sku, qty in items_dict.items():
            order.add_item_to_order(item_sku, qty, self.inventory[item_sku].price)

        # update inventory
        for item_sku, qty in items_dict.items():
            self.inventory[item_sku].qty -= qty

    def display_orders(self):
        print(self.orders)

    # def add_qty(self, sku:str, qty: float):
    #     self.inventory[sku].update_qty(qty)
    #
    # def add_items(self, skus: list, quantities: list):
    #     for sku, qty in zip(skus, quantities):
    #         self.add_qty(sku, qty)
    #
    # def get_products_by_brand(self, brand) -> list[Product]:
    #     ret_val = list()
    #     for product in self.inventory.values():
    #         if product.brand == brand:
    #             ret_val.append(product)
    #     return ret_val
    #
    # def get_out_of_stock(self):
    #     pass
    #
    # def add_order(self):
    #     pass