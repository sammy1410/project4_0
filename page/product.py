import streamlit as st
from utility.fileHandler import ORDER_DB
from utility.fileHandler import USER_DB,user_events_file,user_orders_file
from utility.fileHandler import PRODUCT_DB,PRODUCT_PATH,product_info,product_image,product_data
from utility.shared import this
from utility.timestamp import timestamp
import pickle

product_entry = None

def sendOrder():
    global product_entry
    
    print(product_entry["ID"],product_entry["Name"])
    pass

def layout():
    global product_entry
    product_entry = product_data(this.productID) 
    productID,product_name = product_entry["ID"],product_entry["Name"]

    col1, col2 = st.columns(2)
    with col1:
        st.image(product_image(productID))
    with col2:
        st.header(product_name.upper())
        if "user" in this:
            st.button("Order Item",on_click=sendOrder)
            st.number_input("Quantity",value=1,key="order_qty",min_value=1)
        else:
            st.button("Request Quote")
        with open(product_info(productID),"r") as product_inf: 
            st.text(product_inf.read())
    