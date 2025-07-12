import streamlit as st 

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate it's square, cube, and fifth power")

# Get User Input
n = st.number_input("Enter an Integer", value=1, step=1)

# Calculate Result
square = n**2
cube = n**3
fifth_power = n**5

# Display Result
st.write(f"The suqre of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth_power of {n} is : {fifth_power}")