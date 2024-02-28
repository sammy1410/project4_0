import streamlit as st
from utility.fileHandler import ORDER_DB
from utility.shared import this
import pickle

product_inf_path= "./products/"

def sendOrder():
    print(f"{this.productID}_{this.productName} : Ordered {this.order_qty}")
    pass

def layout():
    product_id,product_name = this.productID,this.productName
    col1, col2 = st.columns(2)
    with col1:
        st.image(f"{product_inf_path}{product_id}_{product_name}/image.jpg")
    with col2:
        st.header(product_name.upper())
        if "user" in this:
            st.button("Order Item",on_click=sendOrder)
            st.number_input("Quantity",value=1,key="order_qty",min_value=1)
        else:
            st.button("Request Quote")
        
        with open(f"{product_inf_path}{product_id}_{product_name}/infoFile","r") as product_inf:
            line = product_inf.read()
            st.text(line)
    