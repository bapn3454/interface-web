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


def main():
    st.title("Login")

    # Registration form
    email = st.text_input("Email")
    password = st.text_input("Password")
    if st.button("Login"):
        # Perform registration logic here
        registered = True
    else:
        registered = False

    # Only show the content if the user is registered
    if registered:
        st.header("Welcome, " + name + "!")
        st.write("This is the hidden content for registered users.")
    else:
        st.warning("Please register to access the content.")

# Function to check if the user is subscribed
def is_user_subscribed():
    # Add your logic here to check the user's subscription status
    return True  # Placeholder logic

# Decorator to restrict access to a page
def restricted_access():
    def decorator(func):
        def wrapper():
            if not is_user_subscribed():
                st.error("Access denied. Please subscribe to access this page.")
            else:
                func()
        return wrapper
    return decorator
    
    
# Call the function to create the footer
create_footer()

if __name__ == '__main__':
    main()
