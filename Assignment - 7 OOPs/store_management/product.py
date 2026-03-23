import logging

#Intialize logging for this module 
logger = logging.getLogger(__name__)

class Product:
    # class defines what data a product has (attributes) and what it can do (methods).
    def __init__(self, name: str, price: float, category : str):
        #intializes product with name, price and category.
        self.name = name #Allows methods to access attributes to when specific object calls 
        self.category = category

        self._price = price # Using '_' prefix signals that this attribute is 'protected'. and stops from direct access,so forcing use of methods to maintain data integrity.

    # Task 2 : Encapsulation (Getters & setters)
    def get_price(self) -> float:
        #getter method for price ->controlled way to read the price
        return self._price
    
    def set_price(self, new_price: float):
        #setter method for validation logic -> validate input before updating data
        if new_price > 0:
            self._price = new_price
            logging.info(f"Price updated successfully for '{self.name}' to INR {self._price:.2f}")
        else:
            # Logging a warning instead of printing -> captured in system logs for debugging without interrupting.
            logging.warning(f"Invalid price update attempted for '{self.name}': INR {new_price}. Price remains INR {self._price:.2f}")

    # Task 6: Magic Methods
    def __str__(self) -> str:
        return f"Product(Name: {self.name}, Category: {self.category},  Price: INR {self._price:.2f})"
    
    def __add__(self, other) -> float:
        # Overloads the '+' operator. This allows to write 'p1 + p2'. improves code readability 
        # check if 'other' is also a Product (or subclass) to avoid errors.
        if isinstance(other, Product):
            return self._price + other._price
        return NotImplemented
    
    #Task 1: Methods
    # Methods encapsulate logic. Instead of manually formatting strings everywhere, the object knows how to describe itself.
    def get_info(self):
        # logs product details.
        # details = f"Product: {self.name} | category: {self.category} | Price: INR {self._price:.2f}" -> for task 6 
        logging .info(self.__str__())

    # lives inside the class so it can access 'self.price' directly.
    def apply_discount(self, percent: float) -> float:
        # calculates and returns the discounted prize
        discount_amount = self._price * (percent/100)
        discounted_val = self._price - discount_amount
        logging.info(f"Applied {percent}% discount to {self.name}. New Price: INR {discounted_val:.2f}")
        return discounted_val
    