import streamlit as st
from utils.logger_config import get_logger
from utils.persistence import save_product, load_inventory

# Initialize Modular Logger
logger = get_logger(__name__)

def render_product_form():
    # encapsulating sidebar form logic -> seprated Ui from execution

    st.title("Product Management System")
    st.write("Fill in the details in the sidebar to add a new product to the view.")

    # --------- SIDEBAR INPUTS ----------
    st.sidebar.header("Add New Product") # -> search way to display then used these sidebar attribute

    # imput  => getting name -> text_input-> unique string
    p_name = st.sidebar.text_input("Product Name", placeholder="Eg -> Something")

    # input => category -> selectbox -> data integrity (categorical strings)
    categories = ["Electronics", "Furniture", "Clothing", "Groceries", "Other"]
    p_category = st.sidebar.selectbox("Category", options = categories)

    # input => price -> number_input -> data integrity (calculations int/float)
    p_price = st.sidebar.number_input("Unit Price (INR)", min_value = 0.0, step=0.01)

    # Month integration for Dashboard Task 4-. hence allowing dashboard to filter products by time.
    months_list = ["January", "February", "March", "April"]
    p_month = st.sidebar.selectbox("Assign to Month", options=months_list)

    # ----- FORM SUBMISSION LOGIC  --------
    # button to add product
    if st.sidebar.button("Add Product"):
        if p_name.strip():

            # Creating Data Product
            new_product = {
                "name": p_name,
                "category": p_category,
                "price": p_price,
                "month":p_month
            }
            # Saving to 'Database'
            save_product(new_product)
            # Execution -> log event
            logger.info(f"New Product Added - Name: {p_name}, Cat: {p_category}, Price: {p_price}")
            # FeedBack
            st.success(f"Successfully added '{p_name}' for month of '{p_month}' to the catalog!")
        else:
            st.error("Product Name is required.")
            logger.warning("Empty product name submission attempted.")

            # Displaing Details
    st.subheader("Current Inventory")
    current_data = load_inventory()
    if current_data:
        # Summary metrics
        total_items = len(current_data)
        total_value = sum(item['price'] for item in current_data)
        col1, col2 = st.columns(2)
        col1.metric("Total Products", total_items)
        col2.metric("Inventory Value", f"INR {total_value:,.2f}")

        # To Display data in tabular form
        st.table(current_data)
    else:
        st.info("The inventory is currently empty. Use the sidebar to add products.")

if __name__ == "__main__":
    render_product_form()