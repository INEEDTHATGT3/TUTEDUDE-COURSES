# Task 1: Safe division utility
# Demonstrating basic exception handling flow using try-except-else-finally

try:
    # Taking user input -> converting to float -> performing divison
    # float() because integers and decimals can be handled
    numerator = float(input(" Enter Numerator: "))
    denominator = float(input(" Enter denominator: "))
    # It will raise a ValueError if user inputs text instead of a number

    result = numerator/ denominator
    # It will trigger ZeroDivisionError if Denominator is 0

except ValueError:
    # handiling non numeric input -> prevents program to crash like did for sys.exit() prreviously
    print("Error: Invalid Input. Please enter numeric values")

except ZeroDivisionError:
    # handiling division by zero -> undefined so will crash 
    print("Error: Nhi ho payega re baba, raju dusra no daal")

else: 
    # Result display -> it ensures prints result only if 'try' succeeded
    print(f"Result: {result}")

finally: 
    # Final status message -> executes no matter what ,suggest end of operation attempt
    print("Operation Complete")

