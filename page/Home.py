import streamlit as st
import os
from utility.shared import this
from utility.shared import file_name

def product_select(location):
    this.pageName="Product"
    this.product=location
    pass

def layout():
    folder_path = "./product_images/"
    
    files = os.listdir(folder_path)

    jpg_files = [file for file in files if file.endswith(".jpg")]

    columnNo = st.slider("No. of Columns",min_value=1,max_value=5)

    columns = st.columns(columnNo)
    col_1,col_2 = st.columns(2)
    i=0
    for jpg_file in jpg_files:
        i=i+1
        if i%2 == 0:    
            with col_1:
                image_path = os.path.join(folder_path, jpg_file)
                st.image(image_path) 
                #print(file_name(jpg_file))               
                st.button(file_name(jpg_file),on_click=product_select,args=(image_path,))
        else:
            with col_2:
                image_path = os.path.join(folder_path, jpg_file)
                st.image(image_path) 
                #print(file_name(jpg_file))               
                st.button(file_name(jpg_file),on_click=product_select,args=(image_path,))
