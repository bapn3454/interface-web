import streamlit as st

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
    
    
text = st.text_area("Enter some text", height=200)

submitted = st.button("Submit")

if submitted:
    st.write("Submit button was clicked!")
    st.write("You entered:")
    st.write(text)





# Call the function to create the footer
create_footer()
