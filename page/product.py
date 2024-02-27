import streamlit as st
import os
from utility.shared import this

def layout():
    st.write("Product Layout")
    if "product" in this:
        product_display(this.product)
    else:
        this.pageName = "Home"

def product_display(product_location):
    print(product_location)
    st.image(product_location)
    pass