import streamlit as st
import csv
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


# Function to read the user data from the CSV file
def read_user_data():
    users = {}
    with open("/home/amal/Documents/Master 2/Projet de synthèse/interface-web/dataset/users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row["email"]
            password = row["password"]
            users[email] = password
    return users

# Check if the user is in the user data dictionary
def is_user_valid(email, password, user_data):
    if email in user_data:
        if user_data[email] == password:
            return True
    return False

def main():
    st.title("Login")

    # Read user data from the CSV file
    user_data = read_user_data()

    # Login form
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check if the user is valid
        if is_user_valid(email, password, user_data):
            # Open the "Accueil" page in the default web browser
            url = "http://localhost:8501/Accueil"
            webbrowser.open_new_tab(url)
        else:
            st.warning("Invalid email or password. Please try again.")
    else:
        st.warning("Please login to access the content.")
        if st.button("Sign Up"):
            # Open the "Accueil" page in the default web browser
            url = "http://localhost:8501/Inscription"
            webbrowser.open_new_tab(url)
    
# Call the function to create the footer
create_footer()

if __name__ == '__main__':
    main()
