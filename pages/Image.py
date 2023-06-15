import base64
import streamlit as st
from PIL import Image
import requests


def process_submit(image):
    url = "https://webhook.site/1eda8b10-2f28-43cd-94ab-e99db2bb3109"
    myobj = {'encoded_image': image}

    response = requests.post(url, json = myobj)
    return response

def create_footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            padding: 10px;
            background-color: #B0E2FF;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="footer"><p>© Copyright iCarus. Tous droits réservés</p></div>',
        unsafe_allow_html=True,
    )
    

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Read the contents of the uploaded file
    file_contents = uploaded_file.read()
    # Encode the file contents to base64
    encoded_file = base64.b64encode(file_contents).decode('utf-8')

else:
    st.write('No image file uploaded.')

submitted = st.button("Submit")

if submitted:
    st.write("Submit button was clicked!")
    # st.write(encoded_file)
    process_submit(encoded_file)


# Call the function to create the footer
create_footer()
