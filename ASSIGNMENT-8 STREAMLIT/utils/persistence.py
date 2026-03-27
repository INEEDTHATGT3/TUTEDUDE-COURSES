import json
import os
from .logger_config import get_logger

logger = get_logger(__name__)
PRODUCT_FILE = "products_inventory.json"

def save_product(product_dict):
    # Appends product record to PRODUCT_FILE.Load existing list -> append -> write back.
    inventory = load_inventory()
    inventory.append(product_dict)
    with open(PRODUCT_FILE, "w") as f:
        json.dump(inventory, f, indent=4)
    logger.info(f"Persisted product: {product_dict.get('name')}")

def load_inventory():
    #Reads all products from PRODUCT_FILE
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, "r") as f:
        return json.load(f)