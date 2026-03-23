#Task 2 : Bill Calculator

prices = [120, 350, 'abc', 500, -200, 800 ,-700, 'cbz']
total_bill = 0

# Iterating through provided list 
for price in prices:
    try:
        # checking negative values -> as prices can't be negativve (duh)
        # manual raising a Value Error to triger execption block 
        if isinstance(price, (int, float)) and price < 0:
            raise ValueError(" Negative price not allowed")
        
        # Adding the price to the running total. This line will naturally raise a TypeError if 'price' is 'abc'
        total_bill += price
        
        # Current Total
        print(f"Added {price} INR. Current Total: {total_bill} INR.")

    except TypeError:
        # Catching non-numeric items. To skip items 'abc' without stopping the calculation for other items.
        print(f"Skipping invalid item '{price}': Not a number.")

    except ValueError as e:
        # Catching the custom raised error for negative numbers. To ensure we don't subtract money from the bill.
        print(f"Skipping invalid item {price}: {e}")

# Final output
print(f"\nFinal Processed Bill Total: {total_bill} INR.")