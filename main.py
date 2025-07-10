from store import Store
from products import Product

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
            active_products = store.get_all_products()
            print("".join(f"\n{index + 1}. {item.show()}"
                          for index, item in enumerate(active_products)))
            print(10 * '-')
        elif choice == "2":
            total_amount = store.get_total_quantity()
            print(f"\ntotal quantity in store: {total_amount}\n")
        elif choice == "3":
            active_products = store.get_all_products()
            print("".join(f"\n{index + 1}. {item.show()}"
                          for index, item in enumerate(active_products)))
            print(10 * '-')

            shopping_list = []

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
                shopping_list.append((selected_product, quantity))
                print(f"Added {quantity} {selected_product.name}(s) to your order.")

                if shopping_list:
                    try:
                        total_price = store.order(shopping_list)
                        print(f"{10 * '*'}\nOrder made successfully!\n"
                              f"Total payment: {total_price}$\n")
                    except Exception as e:
                        print(f"Error processing Order: {e}")
                else:
                    print("No items ordered.")

        elif choice == "4":
            print("Thank you for visiting the store!")
            break  # Exit the main menu loop


def main():
    """Main function with initialized store and products"""
    # Initialize products and store inside main()
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
