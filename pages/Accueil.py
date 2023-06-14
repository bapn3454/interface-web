import streamlit as st
import pandas as pd
import numpy as np
import webbrowser


# Hide pages name on the left sidebar
st.set_page_config(initial_sidebar_state='collapsed')


def create_footer():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px; /* Adjust the height as needed */
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #B0E2FF;
        }
        .footer p {
            margin: 0;
            /*padding-left: 300px;  Adjust the value to add space at the beginning of the text */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="footer"><p>© iCarus. Tous droits réservés</p></div>',
        unsafe_allow_html=True,
    )


# Define the CSS styles for the buttons
button_styles = {
    'button': "background-color: #B0E2FF; padding: 10px 20px; border-radius: 4px; font-size: 16px; width: 665px;",
}



# Add other Streamlit elements
st.title('Welcome to Icarus App')
# Write a paragraph
st.write("Please select the data type that you want to analyze by clicking on the corresponding button above :")

# Add the buttons with the specified styles
button1_clicked = st.button("Write Text")
button2_clicked = st.button("Text + Image")
button3_clicked = st.button("Upload Video")

# Apply styles to the buttons using HTML and CSS
st.markdown(
    f"""
    <style>
    .stButton button {{ {button_styles['button']} }}
    .stButton button:first-child {{ {button_styles['button']} }}
    .stButton button:last-child {{ {button_styles['button']} }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set the custom CSS style for the page
st.markdown(
    """
    <style>
    body {
        background-image: url("sentiment_analysis.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Check if the buttons are clicked
if button1_clicked:
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8501/Text'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    
    
    
if button2_clicked:
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8501/TextImage'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    

if button3_clicked:
    # Add more actions here if needed
    # Define the URL or page you want to navigate to
    url = 'http://localhost:8501/UploadVideo'

    # Open the URL in a new tab or window
    webbrowser.open_new_tab(url)
     # Render the hyperlink to the specified URL
    #st.markdown(f'<a href="{url}" target="_blank"></a>', unsafe_allow_html=True)
    


    

# Call the function to create the footer
create_footer()

