import logging 
from .product import Product #calling class saves us from product.Product

logger = logging.getLogger(__name__)

# electronicProduct will inherit attributes from Product -> name, _price, and category without rewriting them
class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, category: str, warranty_years: int):
        # using super() will refer to parent class (Product) -> DRY(not repeating myself) code
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    #overriding method -> provide warranty_years specific behaviour
    def get_info(self):
        base_info = f"Product: {self.name} | Category: {self.category} | Price: INR {self.get_price():.2f}"
        full_info = f"{base_info} | Warranty: {self.warranty_years} years"
        
        logging.info(full_info)
