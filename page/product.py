import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp,timecode,timeorder,earliestdelivery
import pickle

from database_fold.databaseHandler import productDetails
from utility.fileHandler import product_image,product_description

def sendOrder(qty):
    global product_entry
    try:
        order_data = { 
                    "Name":product_entry["Name"],
                    "Quantity":qty,
                    "Time of Order":timeorder(),
                    "Earliest Delivery Time":earliestdelivery()
            }
            
        with open(user_orders_file(this.user_session["ID"]),"ab") as order_database:
            pickle.dump(order_data,order_database)            
    except:
        st.success("sorry order cannot be placed")
    this.pageName="Home"
    print(product_entry["ID"],product_entry["Name"],qty)
    pass

def layout():
    product = productDetails(this.productID) 

    col1, col2 = st.columns(2)
    with col1:
        st.image(product_image(product.id))
    with col2:
        st.header(str(product.name).upper())
        if "user" in this:
            quantity=st.number_input("Quantity",value=1,key="order_qty",min_value=1)
            if st.button("Order Item",on_click=lambda:sendOrder(quantity)):
                pass
        else:
            st.button("Request Quote")
        with open(product_description(product.id),"r") as product_inf: 
            st.text(product_inf.read())
  
    