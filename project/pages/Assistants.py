# Update your Streamlit code to display a data table
import streamlit as st
import pandas as pd
import requests
st.set_page_config(layout="wide")


st.title('Assistants')

# Replace this URL with the actual URL of your FastAPI backend
FASTAPI_BACKEND = "http://localhost:5050/objects/assistants"

response = requests.get(FASTAPI_BACKEND)
if response.status_code == 200:
    data = response.json()
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    # Make it editable
    # description	oa_name	oa_assistant_id	id	environment	oa_instructions	content	updated_by	created_at	oa_file_ids	roles	active	model	created_by	updated_at
    st.data_editor(
        df,
        column_order = { "oa_name","description","active" },
        column_config = {
            "active":st.column_config.CheckboxColumn(
                "Active.",
                help="This assistant will be used if active.",
                default=False,
            ),
            
        },
        hide_index=True
    )
    # Display the DataFrame as a table in Streamlit

else:
    st.error("Failed to load questions from the backend.")
