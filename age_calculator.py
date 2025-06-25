import streamlit as st
import datetime 

st.title('Age Calculator')
st.write('This app will calculate the age of user')

user_dob = st.date_input('Enter Date of Birth:', min_value=datetime.date(1900, 1, 1))

def calculate_age(user_dob):
    
    user_dob_str = str(user_dob)
    current_year = 2025
    year = ''
    for i in range(4):
        year = year + user_dob_str[i]
    
    return current_year - int(year)

if st.button("Calculate the age"):
    user_age = calculate_age(user_dob)
    st.title(f"Your age is {user_age} years")
    st.success("Your age is calculated")
    