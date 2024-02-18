# Update your Streamlit code to display a data table
import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title('QueryMap')

# Replace this URL with the actual URL of your FastAPI backend
FASTAPI_BACKEND = "http://localhost:5050/objects/querymap"

response = requests.get(FASTAPI_BACKEND)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.data_editor(
        df,
        column_order = {"name","roles","format","query"},
        hide_index=True
    )
else:
    st.error("Failed to load questions from the backend.")


