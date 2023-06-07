import streamlit as st
import cv2

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

uploaded_file = st.file_uploader("Choose a video", type=["mp4"])

if uploaded_file is not None:
    video_bytes = uploaded_file.read()
    video = cv2.VideoCapture(video_bytes)
    st.video(video)
else:
    st.write('No video file uploaded.')

submitted = st.button("Submit")

if submitted:
    st.write("Submit button was clicked!")
    
    
    
    
# Call the function to create the footer
create_footer()
