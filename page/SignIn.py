import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp
from utility.fileHandler import USER_DB,DB_PATH,user_image,user_events_file
import pickle

def toSignUp():
    this.pageName="Sign Up"

def validateUser():
    user = this.email_login
    passw = this.pass_login
    user_exists = False
    pass_correct = False
    with open(USER_DB,"rb") as user_db:
        while True:
            try:
                entry_check = pickle.load(user_db)
                if entry_check["email"] == this.email_login:
                    user_exists = True
                    if entry_check["pass"] == this.pass_login:
                        pass_correct = True
                        this.user_session = entry_check
            except EOFError:
                break
    if not user_exists:
        st.error("User Not Found.")
    else:
        if not pass_correct:
            st.error("Password Incorrect!")
        else:
            this.userLoggedIn = True
            this.user = this.user_session["first_name"]
            with open(user_events_file(this.user_session["ID"]),"a") as user_event:
                 user_event.write(f"User Logged In : {timestamp()}\n")
            if this.user_session["access"] == "Admin":
                this.pageName = "Admin"
            else:
                this.pageName = "Home"
    #if len(user) != 0 :
    #    this.user = user
    #    this.userFileLoc = f"./database/{user}.bin"
    #    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #    this.userFile = open(this.userFileLoc,"a")
    #    this.userFile.write(f"User Login: {timestamp}")
    #    this.userFile.close()


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