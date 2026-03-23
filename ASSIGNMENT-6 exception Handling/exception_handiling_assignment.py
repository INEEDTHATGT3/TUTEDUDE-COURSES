from exception_utils import *

def main():

    # Task 1: Safe Division
    print("\n ------ Task 1: Division Function -------")
    try:
        n = input("Numerator: ")
        d = input("Denominator: ")
        print(f"Result: {safe_divide(n, d)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"{e}")
    finally:
        print("Division Attempt Finished")

 # Task 2: Bill Calculation
    print("\n----- Task 2: Modular Bill Processing ------")
    data = [120, 350, 'abc', 500, -200, 800]
    final_total = calculate_bill(data)
    print(f"Final Validated Bill: INR {final_total}")

    #Task 3: Age Validation
    print("\n------- Task 3: Modular Age Check ------")
    try:
        user_age = int(input("Age ?: "))
        if validate_age(user_age):
            print("Age within insaniyat")
    except ValueError as e:
        print(f"Input Error: {e}")

    # Task 4: File Reader 
    print("\n------ Task 4: Modular File Reader -------")
    fname = input("Enter filename: ")
    try:
        lines = read_safe(fname)
        print("File Preview:", lines)
    except Exception as e:
        print(f"File Error: {e}")
    finally:
        print("File operation attempted.")

    # Task 5: Shopping Cart
    print("\n------- Task 5: Modular Shopping Cart ------")
    cart = []
    while True:
        inp = input("Price (q to quit): ")
        if inp.lower() == 'q': break
        try:
            p = float(inp)
            validate_price(p)
            cart.append(p)
        except ValueError as e:
            print(f"Cart Error: {e}")
    
    print(f"Total Items: {len(cart)} | Total: INR {sum(cart):.2f}")

if __name__ == "__main__": #-> gatekeeping: controling execution
    main()