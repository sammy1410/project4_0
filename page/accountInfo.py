import streamlit as st
from utility.shared import this
from utility.timestamp import timestamp
from utility.fileHandler import DB_PATH, USER_DB, ORDER_DB,user_events_file,user_orders_file,user_image
from utility.fileHandler import write_output,write_mesg,write_error,SCADA_log

def start_SCADA():
    with open(user_events_file(this.user_session["ID"]),"a") as event_file:
        event_file.write(f'{timestamp()}: Logged in to SCADA as UID{this.user_session["ID"]}\n')
    SCADA_log(f'{timestamp()}: Logged in to SCADA as UID{this.user_session["ID"]}\n')
    this.pageName = "SCADA"

def dots():
    dots = str()
    for i in range(len(this.user_session["pass"])):
        dots = dots + "*"

    return dots

def layout():
    if "user_session" in this:
        st.header("Account Information")
        st.image(user_image(this.user_session["ID"]))
        st.write(f'Name: {this.user_session["first_name"]} {this.user_session["last_name"]} ')
        st.write(f'Email: {this.user_session["email"]}')
        st.write(f'Phone: {this.user_session["phone"]}')
        st.write(f'Access Level: {this.user_session["access"]}')
        st.write(f'Password: {dots()}')