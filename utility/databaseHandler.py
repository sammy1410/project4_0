from utility.fileHandler import PRODUCT_DB, PRODUCT_PATH, PRODUCT_NO
from utility.fileHandler import USER_PATH,USER_DB,USER_NO,user_orders_file
from utility.fileHandler import TMP_PATH
from utility.shared import this,change_page
import pickle,shutil
import streamlit as st

   
def totalUsers():
    with open(USER_NO,"r") as file:
        users = int(file.read())
        return users
    
def totalProducts():
    with open(PRODUCT_NO,"r") as file:
        products = int(file.read())
        return products
    
def removeUser():
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

def removeProduct():

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


def showUsers():
    table = list()

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

def showOrders():

    table = list()
    with open(user_orders_file(this.user_session["ID"]),"rb") as orders:
        while True:
            try:
                dt = pickle.load(orders)
                #table = {**table,**dt}
                #dt.pop("ID",None)
                #dt.pop("pass",None)
                table.append(dt)
            except EOFError:
                break
    st.table(table) 

def showProducts():
    table = list()
    with open(PRODUCT_DB,"rb") as users:
        while True:
            try:
                dt = pickle.load(users)
                dt.pop("ID",None)
                table.append(dt)
            except EOFError:
                break
    st.table(table)       
        
