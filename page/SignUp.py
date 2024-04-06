import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp,timecode
from database_fold.databaseHandler import customerEntryExists,addCustomer
from utility.fileHandler import customer_dp

def validateNewUser():
    print(f"""New User Entry: {this.email_signup}""")

    if not customerEntryExists(this.email_signup):
        customer_data = {
                "id": timecode(),
                "firstname": this.firstname_signup,
                "lastname": this.lastname_signup,
                "gender": this.gender_signup,
                "email": this.email_signup,
                "phone": this.phone_signup,
                "password": this.pass_signup,
                "access": this.access_signup
            }
        
        try:
            addCustomer(customer_data)
        except:
            return False

        if this.profile_signup is not None:
                with open(customer_dp(customer_data["id"]),"wb") as profile_img:
                    profile_img.write(this.profile_signup.read())
            
        st.success("User Added! Sign In for more info.")  
        with st.spinner():
            del this.firstname_signup
            del this.lastname_signup
            del this.email_signup
            del this.phone_signup
            del this.gender_signup
            del this.pass_signup
            del this.access_signup
            del this.profile_signup
        this.pageName="Sign In"
    else:
        st.error("User Already Exists. Proceed to Sign In.")

def change_page(page):
    this.pageName = page

def layout():
    st.write("Sign Up")
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

        st.form_submit_button("Sign Up",on_click=validateNewUser)
    st.write("____________________")
    st.text("I'm already a member!")
    st.button("Sign In",on_click=change_page,args=("Sign In",))    
