import streamlit as st
from utils.logger_config import get_logger

logger = get_logger(__name__)

def calculate_discounted_price(price, discounted_pct):
    # application of formula
    return price * (1- (discounted_pct/100))

def run_discount_app():
    st.title("Price Calculator")

    # need to take care of negative no. -> min_value = 0.0 ->.0 set float on default
    orignal_price = st.number_input("Enter Product Price (in INR):, min_value = ", min_value=0.0, step=1.0, value=0.0) 
    # st.slider(label, min, max, default) -> discount percentage
    discount_pct = st.slider("Select Discount Percentage %: ", 0, 50, 10)

    #Trigger buttuon
    if st.button("Calculate Discount"):
        # Logic execution
        final_price = calculate_discounted_price(orignal_price, discount_pct)
        logger.info(f"Input : INR {orignal_price}, Discount: {discount_pct}%, Result: INR {final_price}")

        #Result displaying -> st.success usage for it
        st.success(f"The Final Price after a {discount_pct}% discount is: INR {final_price:,.2f}")

         # Comparison Table Passing list of lists where each inner list work as row.
        comparison_data = [
            ["Original Price", f"INR {orignal_price:,.2f}"],
            ["Discount Amount", f"INR {(orignal_price - final_price):,.2f}"],
            ["Final Price", f"INR {final_price:,.2f}"]
        ]
        
        st.write("------ Comparison Summary ---------")
        st.table(comparison_data)

if __name__ == "__main__":
    run_discount_app()

