import streamlit as st
import pickle
import shutil

from utility.fileHandler import PRODUCT_DB, PRODUCT_PATH, PRODUCT_NO
from utility.fileHandler import USER_PATH,USER_DB,USER_NO
from utility.fileHandler import TMP_PATH

from utility.shared import this 
from utility.databaseHandler import showProducts,showUsers,removeProduct,removeUser,totalProducts,totalUsers

def removeProducts():
    if this.del_product == None:
        print("Product Selected None")
        return
    old_file = open(PRODUCT_DB, "rb")
    temp_file = open(f'{TMP_PATH}productTemp.db',"wb")
    print("Here")
    i=0
    while True:
        try:
            entry = pickle.load(old_file)        
            if i == this.del_product:
                id = entry["ID"]
                print(f"Removing '{PRODUCT_PATH}PID{id}'")
                shutil.rmtree(f'{PRODUCT_PATH}PID{id}')
                with open(PRODUCT_NO,"r") as user:
                    userCount = int(user.read())
                    userCount-=1
                
                with open(PRODUCT_NO,"w") as user:
                    user.write(str(userCount))
                print(f"Deleted Entry: {entry}")
            else:
                pickle.dump(entry,temp_file)
            i+=1
        except EOFError:
            temp_file.close()
            old_file.close()
            shutil.move(f"{TMP_PATH}productTemp.db",PRODUCT_DB)
            break
    
    this.del_product=None
    #removeProduct()

def removeUsers():
    print(this.del_user)
    if this.del_user == None:
        print("User Selected None")
        return
    old_file = open(USER_DB, "rb")
    temp_file = open(f'{TMP_PATH}userTemp.db',"wb")
    i=0
    while True:
        try:
            entry = pickle.load(old_file)
            if i == this.del_user:
                id = entry["ID"]
                print(f"Removing '{USER_PATH}UID{id}'")
                shutil.rmtree(f'{USER_PATH}UID{id}')
                with open(USER_NO,"r") as user:
                    userCount = int(user.read())
                    userCount-=1
                
                with open(USER_NO,"w") as user:
                    user.write(str(userCount))
                print(f"Deleted Entry: {entry}")
            else:
                
                pickle.dump(entry,temp_file)
            i+=1
        except EOFError:
            temp_file.close()
            old_file.close()
            shutil.move(f"{TMP_PATH}userTemp.db",USER_DB)
            break

    this.del_user=None
    #removeUser()


def change_page(page):
    this.pageName=page
    print(f"Change Page: {this.pageName}")


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
            st.button("Delete User Entry",on_click=removeUsers,key="UsersDelete")
        showUsers()

    if ans == "Product Database":
        col1,col2 = st.columns(2)
        with col1:
            st.button("Add new Product",on_click=change_page,args=("New_Product",))
        with col2:
            st.number_input("Select Product Entry",min_value=0,max_value=totalProducts()-1,key="del_product")
            st.button("Delete Product Entry",on_click=removeProducts,key="productDelete")
        showProducts()
