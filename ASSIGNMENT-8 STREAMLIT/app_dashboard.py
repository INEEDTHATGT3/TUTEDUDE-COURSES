import streamlit as st
import os
from utils.logger_config import get_logger
from utils.persistence import load_inventory

# Initialize Logger
logger = get_logger("app_dashboard")

def run_dashboard():
    # 1. Title + Description Header section for "professionalism".huh ah
    st.title("Simple Sales Dashboard")
    st.markdown("""
    This dashboard tracks monthly sales performance and integrates inventory data from **Product Management System**.
    """)

    # 2. Static Data & Month Selection as per question but included name and category to match with database used in task 3
    months = ["January", "February", "March", "April"]
    static_data = [
        {"name": "Base Revenue", "category": "Sales", "price": 1200.0, "month": "January"},
        {"name": "Base Revenue", "category": "Sales", "price": 1500.0, "month": "February"},
        {"name": "Base Revenue", "category": "Sales", "price": 900.0, "month": "March"},
        {"name": "Base Revenue", "category": "Sales", "price": 2000.0, "month": "April"},
    ]

    #Loading generated products from Task 3.
    dynamic_data = load_inventory()
    
    # Merging both datasets.-> To form a complete financial statement (Static + Dynamic).
    combined_data = static_data + dynamic_data

    selected_month = st.selectbox("Select Month to View Performance:", options=months)

    # Summing prices where the month matches (handling both key variations).
    total_month_val = sum(
        item.get('price', 0) for item in combined_data 
        if item.get('month') == selected_month
    )
    
    st.metric(label=f"Total Value for {selected_month}", value=f"INR {total_month_val:,.2f}")
    logger.info(f"Dashboard filtered for: {selected_month}")

    # FINAL BAR CHART -> bar chart showing the sum of (Static + Dynamic) per month.
    st.subheader("Combined Sales Trend (Jan - Apr)")
    
    # Grouping by month and sum prices
    chart_values = []
    for m in months:
        m_total = sum(
            item.get('price', 0) for item in combined_data 
            if item.get('month') == m
        )
        chart_values.append(m_total)

    # ExceptionOnly show if log file exists and is not empty -> although static will remain
    log_file = "app_log.log"
    if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
        st.bar_chart(chart_values)
    else:
        st.warning("Please add a product in 'app_product_form.py' to generate logs and display the chart.")

    # Detailed inventory table
    st.subheader(f"Detailed Breakdown: {selected_month}")
    
    # Filtering combined list for the UI table.
    filtered_list = [
        item for item in combined_data 
        if item.get('month') == selected_month
    ]

    if filtered_list:
        st.table(filtered_list)
    else:
        st.info(f"No data available for {selected_month}.")


if __name__ == "__main__":
    run_dashboard()
