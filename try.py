import streamlit as st
import pandas as pd

# Function to simulate database operations
def store_order(order_data):
    # Simulate storing order data in a database
    st.write("Storing order data:", order_data)

# Sample initial order data
order_data = {
    'Order ID': '123',
    'Product': 'Product A',
    'Quantity': 2,
    'Status': 'Added to Cart'
}

# Display initial order data
st.write("Order Details:")
st.write(pd.DataFrame([order_data]))

# Button to proceed to checkout
if st.button("Proceed to Checkout"):
    # Update order status
    order_data['Status'] = 'Order Placed'

    # Store updated order data
    store_order(order_data)

    # Display updated order data
    st.write("Order Details (Updated):")
    st.write(pd.DataFrame([order_data]))
        

    
