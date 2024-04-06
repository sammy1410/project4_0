import streamlit as st
import pandas as pd

from utility.shared import change_page,this
from database_fold.databaseHandler import customerslimited,productlimited

def showCustomers():
    userTable = list()

    for i in customerslimited(this.customerEntryNo):
        userTable.append(i.all())
    
    df = pd.DataFrame(userTable,columns=["ID","Name","Gender","Email","Phone","Access"])
    st.dataframe(df)

def showProducts():
    productTable = list()

    for i in productlimited(this.productEntryNo):
        productTable.append(i.all())
    
    df = pd.DataFrame(productTable,columns=["ID","Name","Quantity","Price"])
    st.dataframe(df)

def layout():
    st.header("Admin Page")

    tabs = ["Customers Database","Product Database"]
    ans = st.radio("Select Tab", tabs)

    if ans == "Customers Database":
        col1,col2 = st.columns(2)
        with col1:
            st.button("Add new User",on_click=change_page,args=("New_User",))
        with col2:
            st.selectbox("No. of Entries",[5,10,25,50,80],key="customerEntryNo")
        showCustomers()

    if ans == "Product Database":
        col1,col2 = st.columns(2)
        with col1:
            st.button("Add new Product",on_click=change_page,args=("New_Product",))
        with col2:
            st.selectbox("No. of Entries",[5,10,25,50,80],key="productEntryNo")
        showProducts()

#        with col2:
#            st.number_input("Select Product Entry",min_value=0,max_value=totalProducts()-1,key="del_product")
#            st.button("Delete Product Entry",on_click=removeProduct,key="productDelete")
