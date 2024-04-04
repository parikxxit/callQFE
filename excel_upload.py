import streamlit as st
import requests

# Streamlit app title and description
st.title("Upload Excel Sheet")
st.write("Select an Excel file to upload.")

# Streamlit file uploader widget
file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

# Streamlit button to trigger the upload
if st.button("Upload"):
    if file is None:
        st.error("Please upload an Excel file.")
    else:
        # Prepare payload for the POST request
        files = {"file": file}

        # Make a POST request to the backend endpoint
        response = requests.post("https://gleaming-tildy-parikxit.koyeb.app/check-call-quality", files=files)

        # Display the response from the server
        if response.ok:
            st.success("Getting Call Prediction From Uploaded Data")
            st.json(response.json())
        else:
            st.error("Error uploading Excel file. Please try again.")
