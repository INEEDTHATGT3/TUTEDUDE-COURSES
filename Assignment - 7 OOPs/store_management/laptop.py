import logging
from .product import Product

class Laptop(Product):
    def __init__(self, name: str, price: float, category: str, ram: int, storage: int):
        super().__init__(name, price,category)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        #this class by help of polymorphism can be considered as 'Product'
        info = (f"[LAPTOP] {self.name} | RAM: {self.ram}GB | SSD: {self.storage}GB | Price: INR {self.get_price():.2f}")
        logging.info(info)