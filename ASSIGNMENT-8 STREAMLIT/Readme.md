# Assignment 8: Streamlit Based App Development

Author: Dhruv Jaiswal
Course: GenAI
Date: March 26, 2026

- Project Overview
Yeh project ek modular Streamlit based inventory system hai jise Junior Python Developer role ke requirements ko dhyan mein rakh kar banaya gaya hai. Iska main objective simple dashboards bana hai, jo user inputs ko handle kare, aur data ko locally persist (save) kare. maine isme logic, UI, aur storage (JSON) ko alag-alag rakha hai taaki code maintainable rahe.

- Task Details & Logic

1. Basic Streamlit App (app_basic.py)
What: Ek simple greeting application.
Logic: st.text_input se user ka naam input lekar. Jab user st.button click kare, tabhi script greeting display karta hai.
Why: Streamlit ke linear execution flow aur basic widgets ko samajhne ke liye.
2. Price Calculator (app_discount.py)
What: Discount calculation tool.
Logic: st.number_input se original price aur st.slider (0-50%) se discount percentage calculate karta hai. Formula used: final = price x (1-discount/100).
Why: Bounded inputs (sliders) aur mathematical operations ko UI par render karne ke liye.
3. Product Form (app_product_form.py)
What: Inventory Management Form with Sidebar.
Logic: Saare inputs (Name, Category, Price, Month) Sidebar mein present hai. Data submit karne par utils/persistence.py function call hota hai jo data ko products_inventory.json mein save karta hai.
4. Mini Dashboard (app_dashboard.py)
What: Integrated Sales & Inventory Dashboard.
Logic: Yeh app Static Sales Data aur Dynamic Inventory (Task 3 ka data) ko merge karta hai. Month select karne par dono sources se filtered data dikhaya jata hai.
Why: Data aggregation aur conditional visualization (Gated Charts) ke liye.

- How to Run
Dependencies Install Karne ke liye:
pip install streamlit
Project Structure Check Karein: Ensure kare ki utils/ folder mein persistence.py aur logger_config.py files present ho.
Run Command: Terminal/CMD mein niche diye gaye commands run karein:
streamlit run app_basic.py        # Task 1 ke liye
streamlit run app_discount.py     # Task 2 ke liye
streamlit run app_product_form.py # Task 3 ke liye
streamlit run app_dashboard.py    # Task 4 ke liye

- Key Features (Extras)
Modular Logging: maine print ki jagah centralized logging use kiya hai. Saari activities app_log.log mein save hoti hain.
Hybrid Data Merging: Dashboard sirf static numbers nahi dikhata balki aapke add kiye huye products ko bhi calculate karta hai.
Gated Chart Logic: Dashboard ka bar chart tabhi visible hota hai jab app_log.log file mein activity detection ie exception handiling
Direct-to-Data Persistence: products_inventory.json file storage ki wajah se app refresh karne par bhi data delete nahi hota.
Note -> theme file maine Ai se produce karyi hai as mujhe thoda custom theme kaise implement karte hai dekhna tha
