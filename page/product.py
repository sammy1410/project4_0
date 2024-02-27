import streamlit as st
import os
from utility.shared import this

product_inf_path= "./products/"

def layout():
    #st.write("Product Layout")
    if "product" in this:
        product_display(this.product)
    else:
        this.pageName = "Home"

def product_display(product):
    product_id,product_name = product
    st.header(product_name.upper())
    st.image(f"{product_inf_path}{product_id}_{product_name}/image.jpg")
    with open(f"{product_inf_path}{product_id}_{product_name}/infoFile","r") as product_inf:
        line = product_inf.read()
        st.text(line)
        #while line:
        #    st.text(line)
        #    line = product_inf.readline()
    
    if "user" in this:
        st.button("Buy Item")
    else:
        st.button("Request Quote")
    