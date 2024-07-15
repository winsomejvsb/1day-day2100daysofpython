#Write a program that calculates tax of a particular purchase. 
#The user is only allowed to input four (4) items. And then calculate
# and give the total number of items.


def calculate_tax(price, tax_rate=0.07):
    """Calculate the tax for a given price."""
    return price * tax_rate

def main():
    items = []
    tax_rate = 0.07  # Define a tax rate (7% in this example)

    print("Please enter the prices of 4 items:")

    for i in range(4):
        while True:
            try:
                item_price = float(input(f"Enter the price of item {i + 1}: $"))
                items.append(item_price)
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")

    total_price = sum(items)
    total_tax = sum(calculate_tax(price, tax_rate) for price in items)
    total_price_with_tax = total_price + total_tax

    print("\nItem Prices:", items)
    print(f"Total number of items: {len(items)}")
    print(f"Total price before tax: ${total_price:.2f}")
    print(f"Total tax: ${total_tax:.2f}")
    print(f"Total price with tax: ${total_price_with_tax:.2f}")

if __name__ == "__main__":
    main()



# This program includes the following steps:
# Defines a function calculate_tax that calculates the tax for a given price.
# Prompts the user to enter the prices of four items.
# Validates the user input to ensure it's a valid price.
# Calculates the total price, total tax, and total price including tax.
# Prints the item prices, total number of items, total price before tax, total tax, and total price with tax.
# You can run this program, and it will prompt you to enter the prices of four items, then calculate and display the required information.






