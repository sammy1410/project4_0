import streamlit as st
show_element=st.checkbox("show element")

if show_element:
    st.write("this element")