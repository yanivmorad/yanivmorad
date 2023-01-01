class Customer:
    def __init__(self, customer_id, name, address, phone, email=None):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"<Customer>\n" \
               f"ID: {self.customer_id}" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Phone: {self.phone}"

    def __repr__(self):
        return f"<Customer> {self.name}"