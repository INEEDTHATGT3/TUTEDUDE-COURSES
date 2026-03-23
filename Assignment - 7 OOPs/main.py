import logging
from store_management.product import Product
from store_management.electronics import ElectronicProduct 
from store_management.laptop import Laptop
from store_management.mobile import Mobile
from store_management.payment import CreditCardPayment, UPIPayment
from store_management.store import Store
#called class itself from files to reduce no of words

# to defines custom of output and what level of detail i want to show.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

def main():
    # Task 1: Object Creation
    # Creating distinct instances to show that each object can maintain its own state.
    p1 = Product("office chair", 1200.0, "furniture")
    p2 = Product("Wireless Mouse", 50.0, "Accessories")

    logging.info("------ Displaying Products Info -------")
    p1.get_info()
    p2.get_info()

    # Task 2: Testing Encapsulation
    logging.info("------- Testing Price Updates -------")
    
    # Valid Update
    p1.set_price(1150.0) 
    # Invalid Update
    p2.set_price(-10.0) 

    # Verify via Getter
    logging.info(f"Verified Price for {p2.name}: INR {p2.get_price():.2f}")

    #optional Test Case
    p1.apply_discount(15)

    # Task 3: Inheritance & Overriding
    logging.info("\n ------ Task 3 : Inheritance & Override ------")

    # instance of Child class -> 4 arguments
    elec_p = ElectronicProduct("Mobile", 9000, "Electronics", 3)

     
    # apply_discount isn't in electronics.py,it works because it was inherited from product.py.
    elec_p.apply_discount(10)
    
    # calls the OVERRIDDEN version of get_info.
    elec_p.get_info()

    # Task 4: Polymorphism Test Cases 
    #We create a list containing different types of objects.-> Because they all inherit from 'Product', they share the 'get_info' interface.
    catalog = [
        Laptop("Acer Aspire 7", 63000.0, "Electronics", 16, 512),
        Mobile("Mi 11X", 27000.0, "Electronics", 6.67),
        ElectronicProduct("Washing Machine", 500.0, "Appliances", 5)
    ]

    logging.info("----- Iterating through Catalog ------")
    
    for item in catalog:
        # loop just calls 'get_info()', and the object decides how to respond.
        item.get_info()

    # Task 5: Abstraction & Payment Processing
    # just checking if working or not by choosing and passing object from catalog in task 4 
    # as eventually have to make inventory system
    z1 = catalog[0]
    z2 = catalog[1]
    z1.get_info()
    z2.get_info()

    logging.info("\n--- Initiating Payment Systems (Abstraction) ---")
    
    amount_to_pay = p1.get_price()

    # Scenario A: User chooses Credit Card.
    cc_pay = CreditCardPayment()
    cc_pay.process_payment(amount_to_pay)

    # Scenario B: User chooses UPI
    upi_pay = UPIPayment()
    upi_pay.process_payment(amount_to_pay)

    # Task 6 Magic Methods & Operator Overloading
    # Testing Operator Overloading -> Calculating the 'Total Asset Value' of your devices.
    total_asset_value = z1 + z2
    logging.info(f"Combined Value of {z1.name} and {z2.name}: INR {total_asset_value:.2f}")

     # 1. Creating a Store object
    my_store = Store("Dhruv's Inventory service")

    while True:
        print(f"\n{'='*10} MAIN MENU {'='*10}")
        print("1. Add New Product ")
        print("2. Remove Product ")
        print("3. View Store Summary")
        print("4. View All Products (Detailed)")
        print("5. Test Operator Overloading (Combine Prices)")
        print("6. Exit")
        
        cmd = input("\nEnter your choice: ")

        if cmd == "1":
            # Takes input and creates object
            my_store.add_new_product()

        elif cmd == "2":
            # Remove first occurrence
            target = input("Enter the exact name of the product to remove: ")
            my_store.inventory.remove_product(target)

        elif cmd == "3":
            # Showing Summary
            my_store.show_summary()

        elif cmd == "4":
            # Show All Products
            my_store.inventory.show_all_products()

        elif cmd == "5":
            # Using add to combine prices of two products
            products = my_store.inventory.products
            if len(products) >= 2:
                print("\nSelect two products to combine prices:")
                for i, p in enumerate(products):
                    print(f"{i}. {p.name}")
                
                idx1 = int(input("Enter index of first product: "))
                idx2 = int(input("Enter index of second product: "))
                
                # Using the __add__ Magic Method from Task 6
                combined = products[idx1] + products[idx2]
                logging.info(f"Combined Price of {products[idx1].name} and {products[idx2].name}: INR {combined:.2f}")
            else:
                logging.warning("Need at least 2 products in inventory to test overloading.")

        elif cmd == "6":
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
    
if __name__ == "__main__":
    main()