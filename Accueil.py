import streamlit as st
import pandas as pd
import numpy as np
import webbrowser

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


# Add other Streamlit elements
st.title('Welcome to Icarus App')
# Write a paragraph
st.write("Please select the data type that you want to analyze by clicking on the corresponding button above :")

# Define the CSS styling for the button
button_style = """
    <style>
    .custom-button {
        width: 500px;
        height: 50px;
        background-color: #808080;
        color: #FFFFFF;
    }
    </style>
"""

if st.button('Write text'):
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8503/Text'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    
    
    
if st.button('Text + Image'):
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8503/TextImage'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    

if st.button('Upload Video'):
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8503/UploadVideo'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    


# Call the function to create the footer
create_footer()

