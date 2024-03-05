import streamlit as st

st.title('MyBake 2024')

# Section title for the form
st.header('Add a New Shop')

with st.form(key='add_shop_form'):
    shop_name = st.text_input(label='Shop Name:')
    shop_code = st.text_input(label='Shop Code:')
    owner_name = st.text_input(label='Owner Name:')
    contact_person = st.text_input(label='Contact Person:')
    phone_1 = st.text_input(label='Phone 1:')
    phone_2 = st.text_input(label='Phone 2:')
    address = st.text_area(label='Address:')
    gps_latitude = st.text_input(label='GPS Latitude:')
    gps_longitude = st.text_input(label='GPS Longitude:')
    shop_discount = st.text_input(label='Shop Discount:')
    city = st.text_input(label='City:')
    state = st.text_input(label='State:')
    trn = st.text_input(label='TRN:')
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # You can process the data here
    st.write("Shop Name:", shop_name)
    # Process and display other fields similarly...

# Note that when you run the app, you need to handle what happens when the form is submitted.

