import streamlit as st
from utility.fileHandler import USER_DB, PRODUCT_DB
import pickle
import pandas as pd

from utility.shared import this 

def change_page(page):
    this.pageName=page
    print(f"Change Page: {this.pageName}")

def layout():
    st.header("Admin Page")

    tabs = ["Users Database","Product Database"]
    ans = st.radio("Select Tab", tabs)


    ## Create a table showing all the data
    table = list()
    #ans = st.selectbox("Database",("Users Database","Product Database"))
    if ans == "Users Database":
        st.button("Add new User",on_click=change_page,args=("New_User",))
        with open(USER_DB,"rb") as users:
            while True:
                try:
                    dt = pickle.load(users)
                    #table = {**table,**dt}
                    dt.pop("ID",None)
                    dt.pop("pass",None)
                    table.append(dt)
                except EOFError:
                    break
        st.table(table)  
        
    if ans == "Product Database":
        st.button("Add new Product",on_click=change_page,args=("New_Product",))     
        with open(PRODUCT_DB,"rb") as users:
            while True:
                try:
                    dt = pickle.load(users)
                    dt.pop("ID",None)
                    table.append(dt)
                except EOFError:
                    break
        st.table(table)       
        
