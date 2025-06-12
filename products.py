"""
This module defines the `Product` class representing a store product
with attributes like `name`, `price`, and `quantity`.
"""


class Product:
    """
    Represents a product in a store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product. Must be a positive number.
        quantity (int): The quantity of the product in stock. Must be a non-negative integer.
        active (bool): Indicates whether the product is active in the store. Default is True.

    Methods:
        __init__: Initializes a new instance of the Product class,
                    with validation for the attributes.
    """
    def __init__(self, name, price, quantity):
        """
        Initializes a new product instance with the given details.

        Parameters:
            name (str): The name of the product. It cannot be empty.
            price (float): The price of the product. It must be a non-negative number.
            quantity (int): The quantity of the product.
                            It must be a non-negative integer.

        Raises:
            ValueError: If any of the input values are invalid (empty name, negative price or quantity).
        """
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
        return f"{self.name}, Price: {self.price}$, Quantity: {self.quantity}"

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
            return total_price
