import streamlit as st
from utility.shared import this

def pagechange():
    this.pageName="Home"
    print("page changed.")
def layout():
    st.header("This page doesnot exist.")
    st.button("Go back to home",on_click=pagechange)