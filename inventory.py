# inventory.py
# Basic Inventory Management System
# Author: Daniel Flores

inventory = {}

def add_product():
    name = input("Product name: ").strip()
    quantity = int(input("Initial quantity: "))
    inventory[name] = quantity
    print(f"Product '{name}' added successfully.\n")

def show_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return

    print("\nCurrent Inventory:")
    for product, quantity in inventory.items():
        print(f"- {product}: {quantity}")
    print()

def add_stock():
    name = input("Product name: ").strip()
    if name in inventory:
        quantity = int(input("Quantity to add: "))
        inventory[name] += quantity
        print("Stock updated.\n")
    else:
        print("Product not found.\n")

def remove_stock():
    name = input("Product name: ").strip()
    if name in inventory:
        quantity = int(input("Quantity to remove: "))
        if quantity <= inventory[name]:
            inventory[name] -= quantity
            print("Stock updated.\n")
        else:
            print("Not enough stock.\n")
    else:
        print("Product not found.\n")

def main_menu():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Add stock")
        print("4. Remove stock")
        print("5. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_product()
        elif option == "2":
            show_inventory()
        elif option == "3":
            add_stock()
        elif option == "4":
            remove_stock()
        elif option == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main_menu()
