# ASSIGNMENT: MATPLOTLIB VISUALIZATION

Author: Dhruv Jaiswal
Course: GenAI / Data Science
Date: April 20, 2026

- Project Overview
Yeh project ek Data Analyst trainee assignment ka part hai jisme Matplotlib library ka use karke real-world Car Sales data ko visualize kiya gaya hai. Is assignment ka main objective data ke peeche ki "Business Story" ko samajhna tha jaise market trends, inventory velocity, aur pricing strategy. Isme strict constraints follow kiye gaye hain jaise "No Seaborn" aur "No Pandas Plotting" shortcuts.

- Key Features

1. Pure Matplotlib Implementation: Pura visualization matplotlib.pyplot module ka use karke banaya gaya hai bina kisi external high-level wrappers ke.
2. Logging over Printing: Standard print() statements ki jagah professional logging module use kiya gaya hai taaki execution flow track ho sake.
3. Story-Driven Analytics: Har plot sirf ek chart nahi balki car seller ke liye ek decision-making insight (e.g., Value Erosion, Brand Resilience) ke tarah kaam karta hai.

- Task Details & Logic

Task 1 (Line Plot - The Pulse): Sales trend ko months ke basis par visualize kiya taaki Golden Months identify ho sakein jahan buyer activity peak par hoti hai.

Task 2 (Scatter Plot - Performance Audit): Manufacture markup retail (MMR) aur actual Selling Price ko compare kiya. Diagonal line ke through "Wins" (premium sales) aur "Red Flags" (under-valuation) ko audit kiya.

Task 3 (Bar Plots - Inventory Velocity): Vertical aur Horizontal bar charts ke through top brands aur body types ko analyze kiya. Isse "Safe Bets" (high trust brands) aur "Lifestyle Trends" (SUV vs Sedan) ka pata chala.

Task 4 (Multiple Bar - Brand Resilience): 2014 aur 2015 model years ke sales volume ko side-by-side compare kiya. Isse yeh samajh aaya ki kaunse manufacturers ne successfully apne brand value ko "upgrade" kiya hai.

Task 5 (Stacked Bar - Value Erosion): Vehicle condition ko ranges (1-20, 21-40, 41+) mein divide karke price brackets (Budget, Standard, Luxury) par impact dekha.

Task 6 (Histogram - Market Equilibrium): Price distribution analyze karke Sweet Spot find kiya. Isse seller ko pata chalta hai ki "Volume Drivers" ko kis price range mein rakhna chahiye.

Task 7 (Pie Chart - Asset Allocation): Brand-wise market share calculate kiya taaki portfolio risk assess ho sake. Isse car dealer ko idea milta hai ki kis brand par capital invest karna safe hai.

- How to Run
- Prerequisites: Aapke system mein Python environment aur Jupyter Notebook hona chahiye. Install Dependencies:
pip install matplotlib pandas numpy
- Run Notebook: .ipynb file ko open karein aur saare cells ko sequential order mein execute karein.
- Logs: Har task ke completion aur data processing ki details aapko console/output area mein formatted logs ke roop mein dikhenge
