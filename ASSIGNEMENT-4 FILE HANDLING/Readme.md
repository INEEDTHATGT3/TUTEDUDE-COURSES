### Assignment 4 : Python File Handling

Author: Dhruv Jaiswal

Course: GenAI

Date: March 13, 2026

Assignment Overview

Is assignment mein maine Python ke core File Handling concepts ko implement kiya hai. Bina kisi external library (jaise Pandas ya CSV) ke, maine raw text files create karna, unhe read karna, data append karna aur reports generate karna seekha hai.
Focus is baat par thi ki with open() context manager ka use karke safe file operations kaise kiye jaate hain aur different modes (r, w, a) ka data manipulation mein kya role hota hai.

- How to Run

1. Ensure aapke system par Python 3.11.14 installed hai (as per my setup).
2. Is assignment ki script ko kisi bhi Python IDE (VS Code/PyCharm) mein run karein.
3. Files (sales_data.txt, products.txt, discount_report.txt) automatically generate ho jayengi same directory mein.
4. Tasks sequence mein (Task 1 to Task 7) execute honge. Task 5 aur Task 7 interactive hain, toh terminal mein input dena zaroori hai.

``` Task Details & Logic ```
Task 1: Write Sales Records
Logic: sales list ko iterate karke w mode mein file mein likha.
Note: Har sale ke baad \n use kiya hai taaki data separate lines mein dikhe. String conversion (str()) ka use kiya kyunki file sirf text accept karta hai.

Task 2: Reading Methods
Logic: .read(), .readline(), aur .readlines() ka difference demonstrate kiya.
Note: .readlines() se list milti hai, jisme maine list comprehension use karke \n ko strip kiya aur data ko int mein convert kiya for further processing.

Task 3: Append Mode
Logic: Existing file mein bina purana data delete kiye naya data add karne ke liye a mode use kiya.
Note: Append karne ke baad file pointer end mein hota hai, isliye re-read karne ke liye file ko dobara open kiya.

Task 4: Summary Report
Logic: File se data read karke basic mathematical aggregation ki.
Note: sum(), max(), aur min() ka use kiya. Average nikalne ke liye : Total,Count se formula use kiya.

Task 5: Product Info (User Input)
Logic: User se input lekar Pipe (|) delimiter ke saath data store kiya.
Note: Maine input validation lagaya hai; agar price integer nahi hai toh code "input invalid" print karke exit ho jayega (sys.exit()).

Task 6: Safe File Reading
Logic: os.path.exists() use kiya file check karne ke liye.
Note: Ye "Look Before You Leap" (LBYL) approach hai taaki program crash na ho agar user galat filename de de.

Task 7: Mini Project (Discount Export)
Logic: Dictionary data ko process karke discounted values calculate ki aur report generate ki.
Note: Summary section bottom mein add kiya hai with Total Items aur Average Discounted Price, jo real-world invoice generation jaisa hai