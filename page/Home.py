import streamlit as st
import os
from utility.shared import this
from utility.shared import file_name

from utility.fileHandler import PRODUCT_DB,PRODUCT_PATH

def product_select(productid,productName):
    this.productID,this.productName= productid,productName
    this.pageName="Product"
    print(f"Change Page: {this.pageName}")
    pass

def layout():
    files = os.listdir(PRODUCT_PATH)
    #columnNo = st.slider("No. of Columns",min_value=1,max_value=5)
    #columns = st.columns(columnNo)

    col_1,col_2 = st.columns(2)
    i=1
    
    with open(PRODUCT_DB,"r") as product_db:
        line = product_db.readline().strip()
        while line:
            product_id,product_name=line.split(",")
            i=i+1
            if i%2 == 0:    
                with col_1:
                    #image_path = os.path.join()
                    st.image(f"{PRODUCT_PATH}{product_id}_{product_name}/image.jpg") 
                    st.write(product_name.upper())             
                    st.button("Buy", on_click=product_select, args=(product_id, product_name), key=product_id)
                    #st.button("Buy", on_click=product_select, args=(zip(product_id, product_name),), key=product_id)
            else:
                with col_2:
                    st.image(f"{PRODUCT_PATH}{product_id}_{product_name}/image.jpg") 
                    st.write(product_name.upper())         
                    st.button("Buy", on_click=product_select, args=(product_id, product_name), key=product_id)
            line = product_db.readline().strip()
            