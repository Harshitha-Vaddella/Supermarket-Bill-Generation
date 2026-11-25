
from datetime import datetime

# Product catalog
products = {
    "Apple": 99,
    "Banana": 99,
    "Milk": 49,
    "Orange": 60,
    "Bread": 40,
    "Rice": 70
}

# Customer details
customer_name = input("Enter customer name: ")

# Shopping cart
cart = {}

# Function to display products
def display_products():
    print("\n------ AVAILABLE PRODUCTS ------")
    print("Product          Price")
    print("-------------------------------")

    for product, price in products.items():
        print(f"{product:<15} Rs.{price:.2f}")

    print("-------------------------------")


# Function to generate bill
def generate_bill():
    subtotal = 0

    print("\n==============================================")
    print("              FRESH MART")
    print("          Hyderabad, Telangana")
    print("==============================================")
    print("Customer Name:", customer_name)
    print("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("----------------------------------------------")

    if not cart:
        print("No items purchased.")
    else:
        print(f"{'Item':<12}{'Qty':<6}{'Price':<10}{'Total':<10}")
        print("----------------------------------------------")

        for item, quantity in cart.items():
            price = products[item]
            item_total = price * quantity
            subtotal += item_total

            print(f"{item:<12}{quantity:<6}{price:<10.2f}{item_total:<10.2f}")

    tax = subtotal * 0.12
    final_total = subtotal + tax

    print("----------------------------------------------")
    print(f"Subtotal:          Rs.{subtotal:.2f}")
    print(f"Tax (12%):         Rs.{tax:.2f}")
    print(f"Grand Total:       Rs.{final_total:.2f}")
    print("==============================================")
    print("       Thank you for shopping with us!")
    print("==============================================")


# Main program
while True:

    print("\n------ SUPERMARKET BILLING SYSTEM ------")
    print("1. View Products")
    print("2. Add Items to Cart")
    print("3. Generate Bill and Exit")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        display_products()

    elif choice == "2":
        display_products()

        item = input("Enter product name (or 'exit' to go back): ").strip().title()

        if item == "Exit":
            continue

        if item not in products:
            print("Product not available!")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                continue

            cart[item] = cart.get(item, 0) + quantity

            print(quantity, item, "added to cart successfully!")

        except ValueError:
            print("Invalid quantity! Please enter a valid number.")

    elif choice == "3":
        generate_bill()
        break

    elif choice == "4":
        generate_bill()
        break

    else:
        print("Invalid choice! Please try again.")
