import streamlit as st
from utility.shared import this,change_page

def layout():
    st.header("This page doesnot exist.")
    st.button("Go back to home",on_click=change_page,args=("Home",))