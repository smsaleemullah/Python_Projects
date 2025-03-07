import streamlit as st
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 8:
        return "⚠️ Password length must be at least 8 characters!"

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "⚠️ You must select at least one character type!"

    return ''.join(random.choice(char_pool) for _ in range(length))

# Streamlit UI
st.title("🔐 Random Password Generator")

num_passwords = st.number_input("How many passwords do you want to generate?", min_value=1, step=1)
password_length = st.number_input("Enter password length:", min_value=8, step=1)

use_upper = st.checkbox("Include Uppercase Letters")
use_lower = st.checkbox("Include Lowercase Letters")
use_digits = st.checkbox("Include Numbers")
use_symbols = st.checkbox("Include Symbols")

if st.button("Generate Passwords"):
    if num_passwords > 0:
        st.write("### Generated Passwords:")
        for _ in range(num_passwords):
            st.success(generate_password(password_length, use_upper, use_lower, use_digits, use_symbols))
