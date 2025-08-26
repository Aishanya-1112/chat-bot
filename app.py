import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

#before running install dependencies --- pip install streamlit google-generativeai python-dotenv

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


USERNAME = "test"                       

PASSWORD = os.getenv("APP_PASSWORD")     


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Please Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if u == USERNAME and p == PASSWORD:
            st.session_state.authenticated = True
            st.success("Access granted !!")
        else:
            st.error("Access denied !!")
    st.stop()

# ---- Gemini Chat ----
st.title("Chat Bot")

prompt = st.text_area("Enter your prompt:")

if st.button("submit"):
    if prompt.strip():
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        response = model.generate_content(prompt)
        st.write(response.text)
