# Assignment 3: Python Functions

Author: Sambhav Jaiswal
Course: GenAI
Date: March 4, 2026

- Project Overview

> Is assignment mein maine Python ke core function concepts ko implement kiya hai. Starting from basic functions to advanced functional programming tools like map, filter, and lambda.
>> Previous assignment (Assignment 2) ke feedback ko dhyan mein rakhte hue, maine code readability improve ki hai, snake_case conventions follow kiye hain, aur logic ko detail mein explain kiya hai taaki mera problem-solving approach clear dikhe. will improve more as per suggestion provided

- How to Run

1. Ensure aapke system par Python 3.11.14(i used) installed
2. Assignment3.ipynb file ko VS Code ya kisi bhi Jupyter environment mein open karein.
3. Saare cells ko sequence (Task 1 to Task 7) mein run karein.
4. Task 7 is interactive menu, so terminal/console input ka use karein options select karne ke liye.

- Task Details & Logic

1. Task 1: Basic Function (Price After Discount)
Logic: Ek function banaya jo price return karta hai.
Note: Maine discount_percent=5 default value rakhi hai taaki agar user koi value na de, toh 5% automatically apply ho jaye (as per question). Extra condition bhi lagayi hai ki discount 60% se zyada na ho (Safety check).
2. Task 2: Recursive Function (Factorial Utility)
Logic: Recursion use karke factorial calculate kiya.
Note: Base cases handle kiye hain (n=0 or 1). and important, negative numbers ke liye error message print karwaya hai taaki infinite recursion na ho jaye.
3. Task 3 & 4: Lambda & Map (GST Calculator)
Logic: Lambda function for 18% GST and map() for list processing.
Note: Lambda use karne se code kaafi concise ho gaya. Task 4 mein map() use karke ek hi baar mein poori list par GST apply kar diya, jo ki manual loops se fast hai.
4. Task 5: Filter (Expensive Products)
Logic: filter() use karke prices ko categorize kiya.
Note: Yahan maine is_expensive function banaya hai. Previous feedback ke baad maine ensure kiya ki print labels aur logic (Price > 500) match karein. pehle maine galti kari thi
5. Task 6: Combined Utility Function
Logic: Map aur Filter ka combination.
Note: Ek hi function process_prices mein pehle 10% discount apply kiya (Map) aur phir result ko filter kiya (> 300). Error handling ke liye empty list check bhi dala hai.
6. Task 7: Interactive Menu Utility
Logic: While loop aur individual functions (add, average, max).
Note: Ye ek real-world scenario ki tarah hai. Maine input validation lagaya hai taaki agar user string enter kare price ki jagah, toh code crash na kare. Output format mein "INR" use kiya hai for consistency.

- Key Improvements (Based on Feedback)
Documentation: Created this README.md to explain the workflow.
Naming Convention: Followed snake_case for all variables and functions.
Code Quality: Added comments explaining "Why" I used certain logic instead of just "What" the code does.
Cleanliness: Removed all duplicate cells and verified outputs.
