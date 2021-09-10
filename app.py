import streamlit as st
from ikea_name_generator import gen_ikea_name

st.write("""
# IKEA Name Generator
Discover your name had you been born a piece of Swedish furniture.
""")

user_input = st.text_input("Enter your name") 
st.write(f"""
## Your IKEA name is...
# {gen_ikea_name(user_input)}
""")