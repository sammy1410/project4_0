import streamlit as st
from utility.shared import this
from utility.fileHandler import ORDER_DB
from utility.fileHandler import USER_DB,user_events_file,user_orders_file,user_orderplaced_file
from utility.databaseHandler import showOrders,showOrderplaced
import os
import pickle


def pagechange():
    this.pageName="Home"

def checkout():
     st.success("The order has been placed successfully")
   
     with open(user_orders_file(this.user_session["ID"]),"rb") as orders:
            while True:
                try:
                    dt=pickle.load(orders)
                    dt["Status"]="Order Placed"
                    dt["userid"]=this.user_session["ID"]
                
                    with open(ORDER_DB,"ab") as ordersforadmin:
                        pickle.dump(dt,ordersforadmin)  
                    
                    with open(user_orderplaced_file(this.user_session["ID"]),"ab") as ordersplaced:
                        pickle.dump(dt,ordersplaced) 
                except EOFError:
                    break
      
     with open(user_orders_file(this.user_session["ID"]),"wb") as orders:
          pass
     #this.pageName="Home"
             

     

def layout():

        if os.path.getsize(user_orders_file(this.user_session["ID"])) > 0:
            showOrders()
            col1, col2 = st.columns(2)
            with col1:
                st.button("Look for more products",on_click=pagechange)
            with col2:
                  st.button("Proceed to checkout",on_click=checkout)
            #if show_table:
            
                #st.title("Order placed successfully.")
                #st.button("Continue looking for product",on_click=pagechange)
                #print("this module is running.")
        else:
            st.title("There are no product added to cart.")
            st.button("Continue looking for product",on_click=pagechange)
        if os.path.getsize(user_orderplaced_file(this.user_session["ID"])) > 0:
            showOrderplaced()

        
        

    
