import logging
from .inventory import Inventory
from .product import Product
from .laptop import Laptop
from .mobile import Mobile

class Store:
    def __init__(self, store_name:str):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        # Interactive method to create objects based on type.
        print(f"\n------ {self.store_name}: Add New Product -------")
        print("1. Generic Product | 2. Laptop | 3. Mobile")
        choice = input("Select Product Type: ")
        
        name = input("Name: ")
        price = float(input("Price ? (INR): "))
        category = input("Category ?: ")

        # Branching logic to include specific attributes from previous tasks.
        if choice == "2":
            ram = int(input("RAM ? (GB): "))
            storage = int(input("Storage ?(GB): "))
            new_item = Laptop(name, price, category, ram, storage)
        elif choice == "3":
            screen = float(input("Screen Size ?(inch): "))
            new_item = Mobile(name, price, category, screen)
        else:
            new_item = Product(name, price, category)

        self.inventory.add_product(new_item)
        print(f"Successfully added {name} to inventory.")

    def show_summary(self):
        # Prints store Inventory
        count = len(self.inventory.products)
        val = self.inventory.get_total_value()
        print(f"\n{'-'*30}")
        print(f"STORE SUMMARY: {self.store_name}")
        logging.info(f"Total Items: {count}")
        logging.info(f"Total Portfolio Value: INR {val:.2f}")
        print(f"{'-'*30}")
