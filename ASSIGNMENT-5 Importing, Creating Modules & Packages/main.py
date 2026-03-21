# TASK 1
# Method 1 : whole file is imported
import math_utils
# method 2 : Importing specific function as per task
from math_utils import square

# TASK 2
import string_utils

# TASK 4
# similiar way we call panda as pd ,numpy as np and many more generally
import shop_package.discount as disc
# calling core utility
from shop_package.billing import calculate_total
# for applying tax in example
import shop_package.billing as bill

# Test cases : Task 1
print("\n------ Math Utils Tests -------")
x = 10
y = 5
# 1. add function test
sum_result = math_utils.add(x,y)
print(f"Addition Result ({x}+{y}): ", sum_result)
# 2. subtract function test
sub_result = math_utils.subtract(x, y)
print(f"Subtract Result ({x}, {y}): ", sub_result)
# 3. square function test
sq_result = square(x)
print("Square Result ({x}^2): ", sq_result)

# Test Cases: Task 2
print("\n--- String Utils Tests ---")
sample_text = "hello sir, This string verfies code is working" # -> strings are immutable each time new str created  

# Testing capitalization : utility formats correctly
capitalized = string_utils.capitalize_words(sample_text)
print("Capitalized:", capitalized)

# Testing string reversal : verifies the slicing logic works on multi-word strings.
reversed_txt = string_utils.reverse_string(sample_text)
print("Reversed :", reversed_txt)

# Testing word count : confirms the split() logic works -> will use in tokenization (NLP)
count = string_utils.word_count(sample_text)
print(f"Word Count of '{sample_text}':", count)

# TEST CASES -> TASK 4
# Testing All Functions in shop_package

# Data: List of product prices in INR
cart_items = [500, 1200, 350, 800]
print("\n ------- Billing System ---------")

# Function 1: calculate_total ,using function by directing importing
gross_total = calculate_total(cart_items)
print(f"Gross Total: INR {gross_total}")

# Function 2: apply_discount (Using alias 'disc'), Applying a 15% discount. 
seasonal_total = disc.apply_discount(gross_total, 15)
print(f"After 15% Seasonal Discount: INR {seasonal_total}")

# Function 3: flat_discount (Using alias 'disc') .Ex of Applying a loyalty coupon of INR 50.
loyalty_total = disc.flat_discount(seasonal_total)
print(f"After Loyalty Coupon (INR 50 off): INR {loyalty_total}")

# Function 4: apply_tax (Using alias 'bill'). Finally, we apply the 5% government tax to the net amount.
final_invoice = bill.apply_tax(loyalty_total)

print(f"Final Invoice Amount: INR {final_invoice:.2f}")