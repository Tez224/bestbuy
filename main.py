from store import Store
from products import Product

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start(store: Store):
    """Function to start the store menu and handle user interaction."""
    while True:
        print(f"Store Menu\n"
              f"{10 * '-'}\n"
              f"1. List all products\n"
              f"2. Show total amount in store\n"
              f"3. Make an order\n"
              f"4. Quit\n")

        choice = input("Please choose a number: ")

        if choice == "1":
            active_products = best_buy.get_all_products()
            print("".join(f"\n{index + 1}. {item.show()}"
                          for index, item in enumerate(active_products)))
            print(10 * '-')
        if choice == "2":
            total_amount = store.get_total_quantity()
            print(f"\ntotal quantity in store: {total_amount}\n")
        if choice == "3":
            active_products = best_buy.get_all_products()
            print("".join(f"\n{index + 1}. {item.show()}"
                          for index, item in enumerate(active_products)))
            print(10 * '-')

            total_price = 0
            while True:
                product_input = input("Please choose a product: ")

                if product_input == "":
                    break

                if (not product_input.isdigit() or int(product_input) < 1
                        or int(product_input) > len(active_products)):
                    print("Invalid product selection. Please try again.")
                    continue

                selected_product = active_products[int(product_input) - 1]
                amount_input = input("Please enter the amount of the product"
                                     " you would like to order: ")

                if amount_input == "":
                    break

                if not amount_input.isdigit() or int(amount_input) <= 0:
                    print("Invalid quantity. Please enter a positive number.")
                    continue

                quantity = int(amount_input)

                try:
                    price = selected_product.buy(quantity)  # Call buy method on selected product
                    total_price += price  # Add the price of this purchase to the total
                    print(f"Added {quantity} {selected_product.name}(s) to your order. "
                          f"Total: {price}$")
                except Exception as e:
                    print(f"Error: {e}")

            print(f"{10 * '*'}\nOrder made successfully!\n"
                  f"Total payment: {total_price}$\n")

        if choice == "4":
            print("Thank you for visiting the store!")
            break  # Exit the main menu loop


def main():
    """ main function"""
    start(best_buy)


if __name__ == "__main__":
    main()
