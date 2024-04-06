import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp

from utility.fileHandler import customer_dp,default_dp

def dots():
    dots = str()
    for i in range(8):
        dots = dots + "*"

    return dots

def layout():
    if "user_session" in this:
        st.header("Account Information")
        try:
            st.image(customer_dp(this.user_session.id))
        except:
            st.image(default_dp(this.user_session.gender))
        st.write(f'Name: {this.user_session.firstname} {this.user_session.lastname} ')
        st.write(f'Email: {this.user_session.email}')
        st.write(f'Phone: {this.user_session.phone}')
        st.write(f'Access Level: {this.user_session.access}')
        st.write(f'Password: {dots()}')