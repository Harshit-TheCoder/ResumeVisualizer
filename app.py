import streamlit as st

st.title("Welcome to Resume Tool")
st.write("Use the sidebar to navigate to Resume Optimizer or Resume Generator.")


def show_sidebar():
    st.sidebar.title("My Sidebar")
    st.sidebar.write("")
    st.sidebar.write("Resume_Optimizer.py")
    st.sidebar.markdown("[Resume Generator](Resume_Generator.py)")

show_sidebar()