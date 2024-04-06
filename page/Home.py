import streamlit as st
import pickle
from utility.shared import this,file_name,change_page
from utility.shared import file_name

from utility.fileHandler import PRODUCT_DB,PRODUCT_PATH,product_image,product_info

def product_select(productid):
    this.productID= productid
    change_page("Product")
    
def layout():
    col_1,col_2 = st.columns(2)
    i=1
    
    with open(PRODUCT_DB,"rb") as product_db:
        while True:
            try:
                product = pickle.load(product_db)
                product_id,product_name=product["ID"],product["Name"] 
                i=i+1
                if i%2 == 0:    
                    with col_1:
                        st.image(product_image(product_id)) 
                        st.write(product_name.upper())             
                        st.button("Buy", on_click=product_select, args=(product_id,), key=product_id)
                else:
                    with col_2:
                        st.image(product_image(product_id)) 
                        st.write(product_name.upper())             
                        st.button("Buy", on_click=product_select, args=(product_id,), key=product_id)
            except EOFError:
                break