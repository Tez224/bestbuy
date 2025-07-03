"""
This module defines the `Store` class, which represents a store
that holds and manages products.

It allows you to:
- Add products to the store.
- Remove products from the store.
- Retrieve all active products.
- Process orders and calculate total prices.

Classes:
    Store: A class that represents a store with a list of
    products and methods for managing them.
"""

class Store:
    """
    Represents a store with a collection of products.

    Attributes:
        product_list (list): A list of products available in the store.
    """
    def __init__(self, product_list=None):
        """
        Initializes a Store instance with a list of products.

        Parameters:
            product_list (list): A list of products to be added to the store.
            Defaults to an empty list.
        """
        if product_list is None:
            product_list = []
        self.product_list = product_list


    def add_product(self, product):
        """ Adds a product to the store. """
        self.product_list.append(product)


    def remove_product(self, product):
        """ Removes a product from the store. """
        self.product_list.remove(product)


    def get_total_quantity(self):
        """ Returns the quantity of all the products in the store. """
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """ Returns a list of all the products in the store. """
        active_products = [product for product in self.product_list if product.active]
        return active_products


    def order(self, shopping_list):
        """
        Processes an order by calculating the total price for the products in the shopping list.

        :param shopping_list: (list of tuples): A list where each item is a tuple (product, quantity)
        :return: str: A message with the total price for the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return f"total price: {total_price}"
