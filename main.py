import streamlit as st
import requests
import io

def analyze_judgment(file):
    url = 'https://90tdu1l307.execute-api.ap-south-1.amazonaws.com/'
    
    files = {'file': file}
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get('summary'), data.get('time_taken')
    except requests.exceptions.RequestException as e:
        return None, str(e)

st.title('Judgment Summary App')

input_text = st.text_area("Enter the text to analyze")

if st.button('Submit'):
    if input_text:
        # Create an in-memory text file
        file = io.StringIO(input_text)
        file.name = "input.txt"  # Give it a name if required by the API
        summary, time_taken = analyze_judgment(file)
        
        if summary:
            st.write("**Summary:**")
            st.write(summary)
            st.write("**Time Taken:**")
            st.write(time_taken)
        else:
            st.write("Error during API call:", time_taken)
    else:
        st.write("Please enter some text to analyze.")
