# Update your Streamlit code to display a data table
import streamlit as st
import pandas as pd
import requests

from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title('Questions')

# Replace this URL with the actual URL of your FastAPI backend
FASTAPI_BACKEND = "http://localhost:5050/objects/histogram/assistant_messages/question"

response = requests.get(FASTAPI_BACKEND)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.data_editor(
        df,
        column_order = {"question","count"},
        hide_index=True
    )
else:
    st.error("Failed to load questions from the backend.")


FASTAPI_BACKEND = "http://localhost:5050/objects/assistant_messages"

response = requests.get(FASTAPI_BACKEND)
if response.status_code == 200:
    data = response.json()
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)
    text = ', '.join(df['question'].values.tolist())
    wordcloud = WordCloud().generate(text)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(plt)
else:
    st.error("Failed to load questions from the backend.")
