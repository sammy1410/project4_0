import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [30, 25, 35, 40]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
st.table(df)

# Add buttons for each row
for index, row in df.iterrows():
    button_clicked = st.button(f"Delete {row['Name']}")
    if button_clicked:
        # Perform action here, for example, remove the row from the DataFrame
        df.drop(index, inplace=True)

# Display the updated DataFrame
st.table(df)
