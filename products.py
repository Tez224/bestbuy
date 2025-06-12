class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price needs to ne a positive number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity needs to be an positive integer")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """ Gets quantity of product """
        return self.quantity

    def set_quantity(self, quantity):
        """ Sets quantity of product """
        if quantity == 0:
            self.active = False
        else:
            self.quantity = quantity
            self.active = True


    def is_active(self):
        """ Checks if product is active """
        return self.active

    def activate(self):
        """ Activates product """
        self.active = True

    def deactivate(self):
        """ Deactivates product """
        self.active = False

    def show(self):
        """ Shows product information """
        print(f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Checks if product quantity is available, if so, buys product and update quantity
        :returns :price to pay for that quantity of product, if quantity < 0 raise error.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.quantity < quantity:
            self.active = False
            raise Exception("Not enough items in store.")
        else:
            self.quantity -= quantity
            total_price = quantity * self.price
            if self.quantity == 0:
                self.active = False
            return f"Price to pay for quantity of {quantity} item(s): {total_price}$"

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
