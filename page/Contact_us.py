import streamlit as st
import pandas as pd
import numpy as np

def layout():
    st.header('Contact Us', divider='rainbow')
    st.subheader("About Us")
    col1, col2= st.columns(2)
    with col1:
        st.image("./images/abhisek.jpg",caption="Abhisek Chaudary (076BME001)")
        st.image("./images/sameer.jpg",caption="Sameer Timsina(076BME037)")
        pass
    with col2:
        st.image("./images/gangu.jpg",caption="Gangotri Sah (076BME012)")
        st.image("./images/sneha.jpg",caption="Sneha Poudel (076BME042)")
        
        pass
    
    st.subheader("OUR HEADQUARTER")
    st.write("""
    ADDRESS:
        IOE Pulchowk Campus
        Lalitpur, Nepal
    
    CONTACT:
        our_mail@companymail.com
""")
    st.write(f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d883.2818892015782!2d85.31977902093878!3d27.68245218889679!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb19b61be60bab%3A0xc43990ed036b6866!2sDepartment%20of%20Mechanical%20and%20Aerospace%20Engineering%2C%20Pulchowk%20Campus!5e0!3m2!1sen!2snp!4v1708885669732!5m2!1sen!2snp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>', unsafe_allow_html=True)
