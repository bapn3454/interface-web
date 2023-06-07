import streamlit as st
from PIL import Image

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
    
    
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text(text)
else:
    st.write('No text file uploaded.')


uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')
else:
    st.write('No image file uploaded.')

submitted = st.button("Submit")

if submitted:
    st.write("Submit button was clicked!")


# Call the function to create the footer
create_footer()
