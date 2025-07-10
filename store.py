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

    Attributes:
        product_list (list): A list of products available in the store.
    """

    def __init__(self, product_list=None):
        """
        Initializes a Store instance with a list of products.

        Parameters:
            product_list (list): A list of products to be added to the store.
            Defaults to an empty list.
        Raises:
            TypeError: If product_list is not a list or None.
            ValueError: If product_list contains non-Product objects.
        """
        if product_list is not None and not isinstance(product_list, list):
            raise TypeError("product_list must be a list or None")

        if product_list is None:
            product_list = []
        else:
            # Check all items are Product instances
            from products import Product  # Import here to avoid circular imports
            for product in product_list:
                if not isinstance(product, Product):
                    raise ValueError("All items in product_list must be Product instances")

        self.product_list = product_list

    def add_product(self, product):
        """
        Adds a product to the store.

        Parameters:
            product (Product): The product to add to the store.

        Raises:
            TypeError: If product is not a Product instance.
            ValueError: If product is already in the store.
        """
        from products import Product  # Import here to avoid circular imports
        if not isinstance(product, Product):
            raise TypeError("Can only add Product instances to the store")

        if product in self.product_list:
            raise ValueError("Product is already in the store")

        self.product_list.append(product)


    def remove_product(self, product):
        """
        Removes a product from the store.

        Parameters:
            product (Product): The product to remove from the store.

        Raises:
            TypeError: If product is not a Product instance.
            ValueError: If product is not found in the store.
        """
        from products import Product  # Import here to avoid circular imports
        if not isinstance(product, Product):
            raise TypeError("Can only remove Product instances from the store")

        if product not in self.product_list:
            raise ValueError("Product not found in store")

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

        :param shopping_list: (list of tuples): A list where each item
                is a tuple (product, quantity)
        :return: str: A message with the total price for the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
