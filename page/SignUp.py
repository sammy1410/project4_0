import streamlit as st
from utility.shared import this
import pickle
import os
import shutil
from utility.timestamp import timestamp
from utility.fileHandler import USER_DB,DB_PATH,user_events_file,user_orders_file,user_image
from utility.fileHandler import USER_NO,USER_PATH

def validateNewUser():
    print(f"""New User Entry: {this.email_signup}""")
    user_exists = False
    
    with open(USER_DB,"rb") as file:
        while True:
            try:
                entry = pickle.load(file)
                if entry["email"] == this.email_signup:
                    user_exists = True
            except EOFError:
                break
    if not user_exists:
        with open(USER_DB,"ab") as file:
            with open(f"{USER_NO}","r") as userCount:
                this.userCount = int(userCount.readline())
            this.userCount += 1
            with open(f"{USER_NO}","w") as userCount:
                userCount.write(str(this.userCount))
            user_data = {
                "ID": this.userCount,
                "first_name": this.firstname_signup,
                "last_name": this.lastname_signup,
                "gender": this.gender_signup,
                "email": this.email_signup,
                "phone": this.phone_signup,
                "pass": this.pass_signup,
                "access": this.access_signup
            }
            pickle.dump(user_data,file)
            os.makedirs(f"{USER_PATH}UID{user_data['ID']}")
            
            with open(user_events_file(user_data["ID"]),"w") as file:
                file.write(f"""
                    User Created: {timestamp()}
                    UID: {user_data['ID']}
                    User Name: {user_data['first_name']} {user_data['last_name']}
                """)
            
            with open(user_orders_file(user_data["ID"]),"w") as file:
                pass

            if this.profile_signup is not None:
                with open(user_image(user_data["ID"]),"wb") as profile_img:
                    profile_img.write(this.profile_signup.read())
            else:
                if this.gender_signup == "Female":
                    from utility.fileHandler import default_female
                    shutil.copy(default_female,f'{user_image(user_data["ID"])}')
                else:
                    from utility.fileHandler import default_male
                    shutil.copy(default_male,f'{user_image(user_data["ID"])}')

            st.success("User Added! Sign In for more info.")  
            with st.spinner():
                #time.sleep(3)
                del this.userCount
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
    st.button("Sign In",on_click=validateNewUser,args=("Sign In",))    
