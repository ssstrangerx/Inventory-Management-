# This is inventory list
inventory = []

# creating a product dictionary
def create_product(sku, name, quantity):
    if not name.strip():
        print("Error: Product name cannot be empty.")
        return None
    try:
        quantity = int(quantity)
        if quantity < 0:
            print("Error: Quantity must be positive.")
            return None
    except ValueError:
        print("Error: Invalid quantity. Please enter a number.")
        return None

    return {"sku": sku, "name": name, "quantity": quantity}

#inserting the product into inventory
def insert_product(product):
    for item in inventory:
        if item["sku"].lower() == product["sku"].lower():
            print("Error: Product with this SKU already exists.")
            return
    inventory.append(product)
    print(f"Product '{product['name']}' inserted successfully.")

# Function to display inventory
def display_inventory():
    if not inventory:
        print("\n Inventory is empty.")
        return
    print("\n Current Inventory:")
    print("SKU\t\tName\t\tQuantity")
    print("-----------------------------------")
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")

# Function to search by SKU
def search_by_sku(sku):
    for item in inventory:
        if item["sku"].lower() == sku.lower():
            print(f"Found: {item}")
            return
    print("Product not found.")

# Function to search by Name
def search_by_name(name):
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Found: {item}")
            return
    print("Product not found.")

# Function to delete a product by SKU
def delete_product(sku):
    for item in inventory:
        if item["sku"].lower() == sku.lower():
            inventory.remove(item)
            print(f"Product '{item['name']}' deleted successfully.")
            return
    print("Product not found.")

# This is the Main loop for user interaction with our program

def main():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Insert Product")
        print("2. Display Inventory")
        print("3. Search Product by SKU")
        print("4. Search Product by Name")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sku = input("Enter SKU: ")
            name = input("Enter Product Name: ")
            qty = input("Enter Quantity: ")
            product = create_product(sku, name, qty)
            if product:
                insert_product(product)

        elif choice == "2":
            display_inventory()

        elif choice == "3":
            sku = input("Enter SKU to search: ")
            search_by_sku(sku)

        elif choice == "4":
            name = input("Enter Product Name to search: ")
            search_by_name(name)

        elif choice == "5":
            sku = input("Enter SKU to delete: ")
            delete_product(sku)

        elif choice == "6":
            print("Thank you, have a nice day!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
