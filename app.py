import streamlit as st

st.title("My AI Chat App")
st.write("Hello World! This is my deployed Streamlit app!")

# Add a simple input
user_input = st.text_input("Enter your message:")
if user_input:
    st.write(f"You said: {user_input}")