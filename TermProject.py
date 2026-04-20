def add_item(inventory):
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    reorder = int(input("Enter reorder level: "))

    inventory[name] = {
        "quantity": quantity,
        "price": price,
        "reorder": reorder
    }

    print("Item added.")


def view_inventory(inventory):
    if not inventory:
        print("Inventory empty.")
        return

    for item, details in inventory.items():
        print("\nItem:", item)
        print("Quantity:", details["quantity"])
        print("Price:", details["price"])
        print("Reorder:", details["reorder"])


def update_stock(inventory):
    name = input("Enter item name: ")

    if name in inventory:
        amount = int(input("Amount to add: "))
        inventory[name]["quantity"] += amount
        print("Updated.")
    else:
        print("Item not found.")


def record_sale(inventory):
    name = input("Enter item sold: ")

    if name in inventory:
        sold = int(input("How many sold: "))
        inventory[name]["quantity"] -= sold
        print("Sale recorded.")
    else:
        print("Item not found.")


def main():
    inventory = {}

    while True:
        print("\n1 View Inventory")
        print("2 Add Item")
        print("3 Update Stock")
        print("4 Record Sale")
        print("5 Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_inventory(inventory)

        elif choice == "2":
            add_item(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            record_sale(inventory)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()