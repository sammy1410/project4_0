import streamlit as st
import pandas as pd

def main():
    st.title("Displaying a Single Location on a Map")

    # Coordinates for the location you want to show
    latitude = 40.7128  # Example latitude (New York City)
    longitude = -74.0060  # Example longitude (New York City)

    # Create a DataFrame with one row containing the coordinates
    data = pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]})

    # Display the map with the specified location
    st.map(data)

if __name__ == "__main__":
    main()
