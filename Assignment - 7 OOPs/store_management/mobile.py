import logging
from .product import Product

class Mobile(Product):
    def __init__(self, name: str, price: float, category: str, screen_size: float):
        super().__init__(name, price, category)
        self.screen_size = screen_size

    def get_info(self):
       # same fundamentals using polymorphism custom attributes to whole new class is still under 'Products'
        info = (f"[MOBILE] {self.name} | Screen: {self.screen_size} inch | Price: INR {self.get_price():.2f}")
        logging.info(info)
