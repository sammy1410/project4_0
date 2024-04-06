import streamlit as st
from utility.shared import this,file_name,change_page

from utility.fileHandler import product_description,product_image
from database_fold.databaseHandler import productAll

def product_select(productid):
    this.productID= productid
    change_page("Product")
    
def layout():
    col_1,col_2 = st.columns(2)
    i=1

    for product in productAll():
        i=i+1
        if i%2 == 0:    
            with col_1:
                st.image(product_image(product.id)) 
                st.write(str(product.name).upper())             
                st.button("Buy", on_click=product_select, args=(product.id,))
        else:
            with col_2:
                st.image(product_image(product.id)) 
                st.write(str(product.name).upper())             
                st.button("Buy", on_click=product_select, args=(product.id,))