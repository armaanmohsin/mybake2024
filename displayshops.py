import streamlit as st
import requests
import pandas as pd

# Access the token from Streamlit secrets
token = st.secrets["my_secrets"]["authorization_token"]

# Define the API endpoint
url = "http://114.94.74.97.host.secureserver.net:3000/shop"

# Set up the headers with the token
headers = {
    "Authorization": f"Bearer {token}"
}

# Make the request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Assuming the API returns JSON that can be directly converted to a DataFrame
    data = response.json()
    
    # Extract the shops data
    shops_data = data['shops']

    # Convert the shops data to a list if not already
    if not isinstance(shops_data, list):
        shops_data = [shops_data]
    
    # Create a DataFrame with specified headers
    df = pd.DataFrame(shops_data)
    
    # Select and rename the columns as specified
    df = df[['id', 'shop_name', 'shop_address', 'contact_person', 'region', 'phone', 'date']]
    df.columns = ['id', 'Shop Name', 'Shop Address', 'Contact Person', 'Region', 'Phone', 'Date']
    
    # Display the DataFrame as a table
    st.table(df)
else:
    st.error("Failed to fetch data from the API.")
