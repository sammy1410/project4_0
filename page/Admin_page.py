import streamlit as st
import pickle
import shutil

from utility.fileHandler import PRODUCT_DB, PRODUCT_PATH, PRODUCT_NO
from utility.fileHandler import USER_PATH,USER_DB,USER_NO
from utility.fileHandler import TMP_PATH

from utility.shared import change_page
from utility.databaseHandler import showProducts,showUsers,removeProduct,removeUser,totalProducts,totalUsers


def layout():
    st.header("Admin Page")

    tabs = ["Users Database","Product Database"]
    ans = st.radio("Select Tab", tabs)

    ## Create a table showing all the data
    #ans = st.selectbox("Database",("Users Database","Product Database"))
    if ans == "Users Database":
        col1,col2 = st.columns(2)
        with col1:
            st.button("Add new User",on_click=change_page,args=("New_User",))
        with col2:
            st.number_input("Select User Entry",min_value=0,max_value=totalUsers()-1,key="del_user")
            st.button("Delete User Entry",on_click=removeUser,key="UsersDelete")
        showUsers()

    if ans == "Product Database":
        col1,col2 = st.columns(2)
        with col1:
            st.button("Add new Product",on_click=change_page,args=("New_Product",))
        with col2:
            st.number_input("Select Product Entry",min_value=0,max_value=totalProducts()-1,key="del_product")
            st.button("Delete Product Entry",on_click=removeProduct,key="productDelete")
        showProducts()
