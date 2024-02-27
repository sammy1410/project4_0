import streamlit as st
from utility.shared import this
import datetime

def validateUser(user,passw):
    print(f"User: {user} & Password: {passw}\n")
    if len(user) != 0 :
        this.user = user
        this.userFileLoc = f"./database/{user}.bin"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        this.userFile = open(this.userFileLoc,"a")
        this.userFile.write(f"User Login: {timestamp}")
        this.userFile.close()


def layout():
    if "user" not in this:
        with st.form("Login Form"):
            username = st.text_input("Username")
            password = st.text_input("Password",type="password")
            #st.form_submit_button("Login")
            st.form_submit_button("Login",on_click=validateUser,args=(username,password,))
    else:
        st.write(f"Welcome {this.user}")
        pass