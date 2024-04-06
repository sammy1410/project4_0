import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp
from database_fold.databaseHandler import customerEntryExists,getCustomerdata
def toSignUp():
    this.pageName="Sign Up"

def validateUser():
    if customerEntryExists(this.email_login):
        customer = getCustomerdata(this.email_login)
        if customer.password == this.pass_login:
            this.user_session = customer
            this.userLoggedIn = True
            this.user = this.user_session.firstname
            
            if this.user_session.access == "admin":
                this.pageName = "Admin"
            else:
                this.pageName = "Home"
        else:
            st.error("Password incorrect!!!")
    else:
        st.error("User not Found")    
    
def layout():
    if "user" not in this:
        with st.form("Login Form"):
            st.text_input("Email",key="email_login")
            st.text_input("Password",type="password",key="pass_login")
            #st.form_submit_button("Login")
            col1, col2 = st.columns(2)
            with col1:
                pass
                
            with col2:
                pass
        
            st.form_submit_button("Login",on_click=validateUser)
            st.link_button("Forgot Password?",url="https://google.com")
            #st.page_link("Contact_Us")
        st.write("___________________________")
        st.button("Create Account",on_click=toSignUp)

    else:
        this.pageName = "Home"
        pass