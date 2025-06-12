class Store:
    def __init__(self, product_list=None):
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
        return f"total quantity in store: {total_quantity}"


    def get_all_products(self):
        """ Returns a list of all the products in the store. """
        active_products = [product for product in self.product_list if product.active]
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return f"total price: {total_price}"