import streamlit as st
import requests
import re

def clean_text(text):
    # Remove unwanted symbols and extra spaces
    cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Remove all non-word characters except spaces
    cleaned_text = cleaned_text.strip()  # Remove leading and trailing spaces
    return cleaned_text

def analyze_judgment(text):
    url = 'https://90tdu1l307.execute-api.ap-south-1.amazonaws.com/'
    
    payload = {'text': text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get('summary'), data.get('time_taken')
    except requests.exceptions.RequestException as e:
        return None, str(e)

st.title('Judgment Analysis App')

# Create two columns
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("Enter the text to analyze")

if st.button('Submit'):
    if input_text:
        cleaned_text = clean_text(input_text)  # Clean the input text
        summary, time_taken = analyze_judgment(cleaned_text)
        
        with col2:
            if summary:
                st.write("**Summary:**")
                st.write(summary)
                st.write("**Time Taken:**")
                st.write(time_taken)
            else:
                st.write("Error during API call:", time_taken)
    else:
        with col2:
            st.write("Please enter some text to analyze.")
