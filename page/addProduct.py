import streamlit as st
import os, shutil
import pickle
from utility.timestamp import timecode
from utility.shared import this

from database_fold.databaseHandler import addProduct,productEntryExists
from utility.fileHandler import product_description, product_image

def productAdd():
    
    while True:
        product_id = timecode()
        if not productEntryExists(product_id):
            break

    product_data = {
        "id": product_id,
        "name": this.product_name,
        "quantity":this.qty,
        "price": this.price,
    }

    if addProduct(product_data):
        if this.product_image is not None:
            with open(product_image(product_id),"wb") as image:
                image.write(this.product_image.read())
        with open(product_description(product_id),"w") as info:
                    info.write(this.description)
        st.success("Product Added")
        this.pageName = "Admin"
    else:
        st.success("Product Could Not be Added")

def layout():
    st.header("Add New Product")
    with st.form("New Product"):
        st.text_input("Product Name",key="product_name")
        st.number_input("Quantity",key="qty")
        st.number_input("Price",key="price")
        st.text_area("Description",key="description")
        st.file_uploader("Product Image",key="product_image")

        st.form_submit_button("Add",on_click=productAdd)