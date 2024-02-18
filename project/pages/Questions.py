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

    st.title('wordcloud')
    text = ', '.join(df['question'])

    print(text)
    
    wordcloud = WordCloud(background_color='black', mode="RGBA", width=800, height=400).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Removes the axis with ticks and labels
    plt.show()
    st.pyplot(plt)
else:
    st.error("Failed to load questions from the backend.")

st.title('timeseries table')
    
# Replace this URL with the actual URL of your FastAPI backend

FASTAPI_BACKEND = "http://localhost:5050/objects/assistant_messages"
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


st.title('timeseries chart')

FASTAPI_BACKEND = "http://localhost:5050/objects/timeseries/assistant_messages"

response = requests.get(FASTAPI_BACKEND)
if response.status_code == 200:
    data = response.json()
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Check if DataFrame is not empty
    if not df.empty:
        # Plotting
        st.line_chart(df.rename(columns={'created_at': 'index'}).set_index('index'))
    else:
        st.write("No data available to display.")
else:
    st.error("Failed to load questions from the backend.")

