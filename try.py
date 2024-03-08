import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [30, 25, 35],
    'Location': ['New York', 'Paris', 'London']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display table
st.table(df)