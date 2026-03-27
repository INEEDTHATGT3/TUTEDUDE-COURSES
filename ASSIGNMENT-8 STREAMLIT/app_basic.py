import streamlit as st
from utils.logger_config import get_logger

# configuring logger -> To create a persistent record for debugging. ->now called instead of writing again
logger = get_logger(__name__)

def run_basic_app():
    # Displaying title
    st.title("Streamlit is alive!")
    logger.info("Application title rendered.")

    # Text Input for Name
    user_name = st.text_input("Enter your name: ")

    # Button Logic and Greeting
    if st.button("Greet Me"):
        if user_name.strip():
            greeting_text = f"Hello, {user_name}!"
            st.write(greeting_text)
            logger.info(f"Greeting successful for user: {user_name}") #logging success
        else:
            st.write("Please enter a name before clicking the button.")
            logger.warning("Greet Me clicked with empty input.") #Logging error

if __name__ == "__main__":
    run_basic_app()