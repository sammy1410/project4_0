import streamlit as st
from utility.shared import this,change_page
from utility.fileHandler import ORDER_DB
from utility.fileHandler import USER_DB,user_events_file,user_orders_file
from utility.databaseHandler import showOrders
import os

def checkout():
     st.success("The order has been placed successfully")
     
     this.pageName="Home"
             

def layout():
        if os.path.getsize(user_orders_file(this.user_session["ID"])) > 0:
            showOrders()
            st.button("Proceed to checkout",on_click=checkout)
            #if show_table:
            
                #st.title("Order placed successfully.")
                #st.button("Continue looking for product",on_click=pagechange)
                #print("this module is running.")
                
        else:
            st.title("There are no order placed.")
            st.button("Continue looking for product",on_click=change_page,args=("Home",))
        

    
