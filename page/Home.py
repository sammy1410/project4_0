import streamlit as st
import os
from utility.shared import this
from utility.shared import file_name

def product_select(location):
    this.pageName="Product"
    this.product=location
    pass

def layout():
    folder_path = "./products/"
    files = os.listdir(folder_path)
    
    #columnNo = st.slider("No. of Columns",min_value=1,max_value=5)
    #columns = st.columns(columnNo)

    col_1,col_2 = st.columns(2)
    i=1
    
    with open(f"{folder_path}product_database","r") as product_database:
        line = product_database.readline().strip()
        while line:
            product_id,product_name=line.split(",")
            i=i+1
            if i%2 == 0:    
                with col_1:
                    #image_path = os.path.join()
                    st.image(f"{folder_path}{product_id}_{product_name}/image.jpg") 
                    st.write(product_name.upper())             
                    st.button("Buy",on_click=product_select,args=(zip(product_id,product_name),),key=product_id)
            else:
                with col_2:
                    st.image(f"{folder_path}{product_id}_{product_name}/image.jpg") 
                    st.write(product_name.upper())             
                    st.button("Buy",on_click=product_select,args=(zip(product_id,product_name),),key=product_id)
            line = product_database.readline().strip()
            