# Assignment 7: Object-Oriented Programming (OOP)

Author: Dhruv Jaiswal
Course: GenAI 
Date: March 17, 2026

- Overview
Is assigment mai ek modular Inventory Management System banaya hai jo ek electronics store ke products, pricing, aur stock ko manage karne ke liye banaya hai. Is assignment ka main focus Python (kyuki C++ mai funcion overloading kara tha yeh magic method pehli bar suna) ke Object-Oriented Programming (OOP) principles ko real-world scenario (jaise billing aur inventory) mein apply kara.

- Key Features & Implementation

1. Modular Architecture: Poora code store_management package mein divided hai. Har task ke liye separate modules (product.py, laptop.py, mobile.py, etc.) use kiye gaye hain taaki code clean aur scalable rahe.
2. Encapsulation: Products ka price _price (protected) rakha gaya hai. Isse direct access restrict karke Getter (get_price) aur Validation-based Setter (set_price) ke through data integrity maintain ki gayi hai.
3. Inheritance: Product base class se Laptop aur Mobile classes inherit karti hain, jisme unke specific attributes (jaise RAM, Storage, Screen Size) add kiya hain.
4. Polymorphism: get_info() method ko override kiya hai taaki har product type (Laptop/Mobile) apni details apne unique style mein display kar saku.
5. Magic Methods & Operator Overloading:
__str__: Readable string representation ke liye.
__add__: Do products ke prices ko directly + operator se add karne ke liye.
6. Interactive Store: main.py ek interactive CLI provide karta hai jahan user khud products add kar sakta hai, summary dekh sakta hai, aur total value calculate kar sakta hai.

- Important Notes
Restrictions & Feedback: Maine is project mein Exceptions aur File Handling ka use avoid kiya hai jaisa ki restrictions mein suggested tha. Par feedback ko dhyan mein rakhte hue, maine Packages aur Modules implement kiye hain taaki code production-ready dikhe. aur .toml file bhi include kari kyuki package install kar sake
Exclusions: Requirements ke hisaab se is implementation mein Abstraction logic ko include nahi kiya Task 7 mai.
Fruitful Learning: Yeh assignment kaafi lengthy tha par mere liye bohot fruitful raha. Isse mere OOPs ke fundamental concepts (specially inheritance aur magic methods) kaafi strong aur revise hogye hain. Thank you