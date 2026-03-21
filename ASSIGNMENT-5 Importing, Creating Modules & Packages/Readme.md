
# Assignment 5: Python Modules & Packages

Author: Dhruv Jaiswal
Course: GenAI / Data Science Foundation
Date: March 17, 2026

- Assignment Overview
Is assignment mein maine Python ke Modules aur Packages architecture ko implement kiya hai. is project se maine seekha ki kaise code ko reusable aur scalable banaya jaata hai.

Focus is baat par thi ki logic ko main.py se nikaal kar dedicated .py files mein kaise rakha jaaye aur __init__.py ka use karke ek professional package structure kaise create kiya jaaye.

- How to Run

1. Ensure aapke system par Python 3.11.14 installed hai.(mine current version)
2. Terminal ya Command Prompt open karein aur modules_assignment/ folder mein jayein.
3. Saare tasks ko test karne ke liye niche di gayi command run karein: python main.py
4. Output terminal mein properly formatted dikhega, jisme Math, String, aur Billing utilities ke results honge.

- Task Details & Logic

1. Task 1: math_utils.py (Simple Module)
Logic: Basic arithmetic functions (add, subtract, square) ko ek separate module mein rakha.

2. Task 2: string_utils.py (String Manipulation)
Logic: Text processing ke liye functions banaye jo capitalization, reversal, aur word count handle karte hain.
Learning: String slicing [::-1] ka use reversal ke liye aur .split() ka use word counting ke liye kiya.

3. Task 3: shop_package (Package Creation)
Logic: discount.py aur billing.py ko ek folder mein daal kar __init__.py file create ki.
Learning: __init__.py is folder ko ek "Package" bana diya. Maine relative imports (from .discount import ...) use kiye taaki package ke functions ko directly access kiya ja sake.

4. Task 4: Integration in main.py
Logic: Aliasing (import ... as disc) aur selective imports ka use karke ek mini-billing system simulate kiya.
Learning: Aliasing ka fayda ye hai ki code readable rehta hai (jaise pandas ko pd likhte hain). Maine sequential logic apply kiya: Total calculate kiya -> Discount lagaya -> Tax apply kiya.

- Expected Output Format
------ Math Utils Tests -------
Addition Result (10+5):  15
Subtract Result (10, 5):  5
Square Result ({x}^2):  100

--- String Utils Tests ---
Capitalized: Hello Sir, This String Verfies Code Is Working
Reversed : gnikrow si edoc seifrev gnirts sihT ,ris olleh
Word Count of 'hello sir, This string verfies code is working': 8

 ------- Billing System ---------

Gross Total: INR 2850
After 15% Seasonal Discount: INR 2422.5
After Loyalty Coupon (INR 50 off): INR 2372.5
Final Invoice Amount: INR 2491.12
