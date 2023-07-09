from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity, price):
        if item not in self.items:
            self.items[item] = {"price": price, "quantity": quantity}
            print(f"Added {quantity} {item}(s) to the transaction.")
        else:
            print(f"Item '{item}' is already added. To update the quantity, use the 'update' option.")

    def update_item_quantity(self, item, quantity):
        if item in self.items:
            self.items[item]["quantity"] = quantity
            print(f"Updated quantity of {item} to {quantity}.")
        else:
            print(f"Item '{item}' is not added to the transaction.")

    def update_item_price(self, item, price):
        if item in self.items:
            self.items[item]["price"] = price
            print(f"Updated price of {item} to {price}.")
        else:
            print(f"Item '{item}' is not added to the transaction.")

    def delete_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Deleted item '{item}' from the transaction.")
        else:
            print(f"Item '{item}' is not added to the transaction.")

    def calculate_total_price(self):
        total_price = 0
        for item, item_data in self.items.items():
            price = item_data["price"]
            quantity = item_data["quantity"]
            total_price += price * quantity
        return total_price

    def apply_discount(self, total_price):
        discount = 0
        if total_price > 200_000:
            if total_price > 300_000:
                discount = 5
            elif total_price > 500_000:
                discount = 8
            else:
                discount = 10

        discount_amount = total_price * (discount / 100)
        return total_price - discount_amount, discount_amount

    def display_transaction_details(self):
        data = [["Item", "Quantity", "Price per Item", "Total Price"]]
        for item, item_data in self.items.items():
            price = item_data["price"]
            quantity = item_data["quantity"]
            total_price = price * quantity
            data.append([item, quantity, price, total_price])

        table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
        print(table)

    def reset(self):
        self.items = {}
        print("Transaction has been reset.")

# Create a transaction instance
transaction = Transaction()

print("== Super Cashier ==")

while True:
    print("\nWhat would you like to do?")
    print("Enter:")
    print("'add' to add an item")
    print("'check' to view transaction details")
    print("'update' to update an item or quantity")
    print("'delete' to delete an item")
    print("'cancel' to reset the transaction")
    print("'done' to finish")

    choice = input("Your choice: ")

    if choice.lower() == "add":
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per item: "))
        transaction.add_item(item, quantity, price)
        print()
    elif choice.lower() == "check":
        print("\nTransaction Details:")
        transaction.display_transaction_details()
    elif choice.lower() == "update":
        print("\nItem Update:")
        item = input("Enter the item name you want to update: ")
        update_choice = input("Enter 'quantity' to update the quantity or 'price' to update the price: ")
        if update_choice.lower() == "quantity":
            quantity = int(input("Enter the new quantity: "))
            transaction.update_item_quantity(item, quantity)
            print()
        elif update_choice.lower() == "price":
            price = float(input("Enter the new price: "))
            transaction.update_item_price(item, price)
            print()
        else:
            print("Invalid update choice. Please try again.")
    elif choice.lower() == "delete":
        item = input("Enter the item name you want to delete: ")
        transaction.delete_item(item)
        print()
    elif choice.lower() == "cancel":
        transaction.reset()
        print()
    elif choice.lower() == "done":
        break
    else:
        print("Invalid choice. Please try again.")

# Calculate the total price
total_price = transaction.calculate_total_price()

# Display the transaction details
print("\nTransaction Details:")
transaction.display_transaction_details()

# Apply the discount
final_price, discount_amount = transaction.apply_discount(total_price)

# Display the total price and discounted price
print(f"Price before discount : Rp {total_price}")
print(f"Discount Amount: Rp {discount_amount}")
print(f"Final price : Rp {total_price - discount_amount}")