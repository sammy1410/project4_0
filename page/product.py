import streamlit as st
from utility.fileHandler import ORDER_DB
from utility.fileHandler import USER_DB,user_events_file,user_orders_file
from utility.fileHandler import PRODUCT_DB,PRODUCT_PATH,product_info,product_image,product_data
from utility.shared import this
from utility.timestamp import timestamp,timecode,timeorder,earliestdelivery
import os

import pickle

product_entry = None

def sendOrder(qty):
    global product_entry
    try:
        with open(user_orders_file(this.user_session["ID"]),"ab") as order_database:
            order_data = { 
                    "Name":product_entry["Name"],
                    "Quantity":qty,
                    "Time of Order":timeorder(),
                    "Earliest Delivery Time":earliestdelivery()
            }
            pickle.dump(order_data,order_database)
            print("Done?")            
    except:
        st.success("sorry order cannot be placed")
    this.pageName="Home"
    print(product_entry["ID"],product_entry["Name"],qty)
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
            quantity=st.number_input("Quantity",value=1,key="order_qty",min_value=1)
            if st.button("Order Item",on_click=lambda:sendOrder(quantity)):
                pass
        else:
            st.button("Request Quote")
        with open(product_info(productID),"r") as product_inf: 
            st.text(product_inf.read())
  
    