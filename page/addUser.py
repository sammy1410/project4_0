import streamlit as st
from utility.shared import this
from page.SignUp import validateNewUser 

def addUser():
    validateNewUser()
    this.pageName="Admin"

def layout():
    with st.form("Sign_Up"):
        col1,col2 = st.columns(2)
        with col1:    
            st.text_input("First Name",key="firstname_signup")
        with col2:
            st.text_input("Last Name",key="lastname_signup")
        st.radio("Gender",("Male","Female","Others"),key="gender_signup")
        st.text_input("Email Address",key="email_signup")
        st.text_input("Phone No.",key="phone_signup")
        st.text_input("Password",type="password",key="pass_signup")
        st.radio("Access Level",("Admin","User"),key="access_signup")
        st.file_uploader("Upload Profile Picture",type=["png","jpg","jpeg"],key="profile_signup")
        st.checkbox("I agree to Terms and Conditions.")

        st.form_submit_button("Sign Up",on_click=addUser)

