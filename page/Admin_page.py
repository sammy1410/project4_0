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

    ## Create a table showing all the data
    table = list()
    table_head = ["ID", "First Name", "Last Name", "Gender","Email", "Phone","Password","Access"]
    ans = st.selectbox("Database",("Users Database","Product Database"))
    if ans == "Users Database":
        with open(USER_DB,"rb") as users:
            while True:
                try:
                    dt = pickle.load(users)
                    #table = {**table,**dt}
                    table.append(dt)
                except EOFError:
                    break
        st.table(table)  
        st.button("Add new User",on_click=change_page,args=("New_User",))     

    if ans == "Product Database":
        with open(PRODUCT_DB,"rb") as users:
            while True:
                try:
                    dt = pickle.load(users)
                    table.append(dt)
                except EOFError:
                    break
        st.table(table)       
        st.button("Add new Product",on_click=change_page,args=("New_Product",))     
