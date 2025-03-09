import streamlit as st # import the Streamlit library
import random # library of python  to generate random numbers
import string # library of python to generate string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters # add letters (both lowercase and uppercase)
    if use_digits:
        characters += string.digits # add digits (e.g. 0-9)
    if use_special:
        characters += string.punctuation # add special characters (e.g. !@#$%^&*)

    return ''.join(random.choice(characters) for _ in range(length))
        
st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: '{password}'")

st.write("---------------------------")

st.write("Made with ❤️ by [Ishaq Niazi]")