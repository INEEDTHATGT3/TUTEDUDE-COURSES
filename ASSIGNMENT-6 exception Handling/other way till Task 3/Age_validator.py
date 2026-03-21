#Task 3: Custom Exception : Age Validator
#enforcing logical constraints using 'raise'

# Validation Function
def check_age(age):
    # if out of range -> ValueError
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    #if pass -> true , else exits functions
    return True

try:
    # Taking user input -> int() conversion () -> second check
    user_input = int(input("Please enter your age: "))
    check_age(user_input)
    print(f"Access Granted: For citizen of Age {user_input}")

except ValueError as e:
    # WHY: 'e' will contain either the system message (for non-integers) 
    # or our custom message (for out-of-range ages).
    print(f"Validation Error: {e}")

finally:
    # ending process
    print("Age verification process concludes")
