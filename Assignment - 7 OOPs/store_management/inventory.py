import logging

class Inventory:
    def __init__(self):
        #empty list to store Product Objects
        self.products = []

    def add_product(self, product):
        #adds product in list
        self.products.append(product)
        logging.info(f"Added to inventory: {product.name}")

    def remove_product(self, name: str):
        # Removes product first occurence by its name. -> iterate for first match -> deletes it -> exiting 
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                logging.info(f"Inventory: Removed first occurrence of '{name}'")
                return
        logging.warning(f"Inventory: Product '{name}' not found.")


    def get_total_value(self) -> float:
        # Calculates total value using the __add__ logic or summation.-> the use of our price getter for the whole list.
        total = sum(p.get_price() for p in self.products)
        return total

    def show_all_products(self):
        # Prints info for every product in the list.    
        if not self.products:
            logging.info("Inventory is empty.")
            return
        
        logging.info("------ Current List -------")
        for p in self.products:
            # This calls the __str__ magic method i defined in Task 6.
            logging.info(p)