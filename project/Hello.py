# Update your Streamlit code to display a data table
import streamlit as st
import pandas as pd
import requests
st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")  # Assuming you have a style.css file with your custom CSS

st.title('Hello')
