import streamlit as st
import os, shutil
import pickle
from utility.timestamp import timecode
from utility.shared import this
from utility.fileHandler import PRODUCT_DB,PRODUCT_NO, PRODUCT_PATH, product_data, product_image, product_info


def productAdd():
    try:
        with open(PRODUCT_DB,"ab") as product_database:
            with open(f"{PRODUCT_NO}","r") as productCount:
                this.productCount = int(productCount.readline())
            this.productCount += 1
            with open(f"{PRODUCT_NO}","w") as productCount:
                productCount.write(str(this.productCount))
            product_data = {
                    "ID": timecode(),
                    "Name": this.product_name
            }
            pickle.dump(product_data,product_database)
            os.makedirs(f"{PRODUCT_PATH}PID{product_data['ID']}")
            
            
            if this.product_image is not None:
                with open(product_image(product_data['ID']),"wb") as image:
                    image.write(this.product_image.read())
            else: 
                from utility.fileHandler import default_product
                shutil.copy(default_product,f'{product_image(product_data["ID"])}')
            
            with open(product_info(product_data['ID']),"w") as info:
                info.write(this.description)
        st.success("Product Added")
        this.pageName = "Admin"
    except:
        st.success("Product Could Not be Added")



def layout():
    st.header("Add New Product")
    with st.form("New Product"):
        st.text_input("Product Name",key="product_name")
        st.text_input("Quantity",key="qty")
        st.text_area("Description",key="description")
        st.file_uploader("Product Image",key="product_image")

        st.form_submit_button("Add",on_click=productAdd)