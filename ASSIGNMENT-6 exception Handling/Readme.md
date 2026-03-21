# Assignment 6:  exception_handling

Author: Dhruv Jaiswal
Course: GenAI
Date: March 20, 2026

- Project Overview
Yeh project Python ka Exception Handling concepts ko deeply cover karne ke liye banaya hai. Starting mein Task 1 se 3 tak strict restrictions kar raha tha (no modules, no file handling), par Task 4 ki requirement aur previous assignment feedback ko incorporate karte huye, iski ek Professional Modular Package mein convert kardiya (feedback suggested to include .toml and submission suggested to include main file).

Isme try-except-else-finally blocks, custom raise exceptions, aur modular structure ka use kara hai -> helps to bulid pipelines (i guess)

- Key Features & Feedback Integration
Modular Structure: Code ko reusable modules (validators, calculators, file_ops) mein divide kiya then.
Export Control: exception_utils/__init__.py mein __all__ ko use karke sirf zaroori functions ko expose kiya , jaisa ki previous feedback mein suggest kiya gaya tha.
Package Configuration: pyproject.toml file include kari for modern package distribution and metadata management.
Safe File Handling: Task 4 ke liye with open() context manager ka use kiya hai taaki file handles safely close ho sakein.
Entry Point Logic: if __name__ == "__main__": block use kiya hai taaki driver script safely run ho sake without side effects during imports.
Project Structure

1. exception_handling_project/

structure
1.1 pyproject.toml # Package metadata aur build instructions-> Ai helped
1.2 exception_utils/ # Core Logic Package
   1.1.1 __init__.py # __all__ -> export control
   1.1.2 validators.py # Age aur Price validation logic (Task 3, 5)
   1.1.3 calculators.py # Division aur Billing logic (Task 1, 2)
   1.1.4file_ops.py   # File handling with exceptions (Task 4)
1.3 exception_handling_assignment.py  # Main Driver File (Task execution)

Task Breakdown:

- Task 1: Safe Division Utility
Logic: Numerator aur Denominator ka input lekar division perform karta hai.
Exceptions: ValueError (invalid input) aur ZeroDivisionError (denominator = 0) ko handle karta hai.

- Task 2: Bill Calculator
Logic: Ek mixed list [120, 350, 'abc', 500, -200, 800] ko process karta hai.
Exceptions: TypeError (non-numeric items) ko skip karta hai aur negative values par custom ValueError raise karta hai.

- Task 3: Age Validator
Logic: check_age(age) function use karke validate karta hai ki age 1 se 120 ke beech hai ya nahi.
Exceptions: Out of range hone par custom message ke saath ValueError raise karta hai.

- Task 4: File Reader
Logic: User se filename lekar uski pehli 3 lines read karta hai.
Exceptions: FileNotFoundError aur PermissionError ko handle karta hai.

- Task 5: Safe Shopping Cart (Mini Program)
Logic: Loop ke andar user se prices leta hai jab tak 'q' na enter ho.
Exceptions: Invalid strings aur negative prices ko handle karke final total aur item count dikhata hai.

- Installation & Usage
Environment Setup: Ensure aapke environment par Python 3.11.8 installed hai.
Running the Script: Terminal open karein aur project directory mein jaakar run karein:
python exception_handling_assignment.py

Installing as a Package (Optional): pyproject.toml -> app local library ke tarah install kar sakte hai
pip install .
