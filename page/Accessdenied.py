import streamlit as st
from utility.shared import this

def pagechange():
    this.pageName="Home"
    print("page changed.")


def layout():
    st.error("Access Denied")
    st.button("Go to home page",on_click=pagechange)