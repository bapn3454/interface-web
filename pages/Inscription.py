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


def main():
    st.title("Create account")

    # Registration form
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password")
    if st.button("Submit"):
        # Perform registration logic here
        registered = register_user(name, email, password)
        # Open the "Accueil" page in the default web browser
        url = "http://localhost:8501/Connexion"
        webbrowser.open_new_tab(url)
    else:
        registered = False


# Function to register a new user
def register_user(name, email, password):
    # Check if the user already exists in the CSV file
    if is_user_existing(email):
        st.warning("User with the same email already exists.")
        return False

    # Write the new user information to the CSV file
    with open("/home/amal/Documents/Master 2/Projet de synthèse/interface-web/dataset/users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])

    return True
    
# Function to check if the user already exists in the CSV file
def is_user_existing(email):
    with open("/home/amal/Documents/Master 2/Projet de synthèse/interface-web/dataset/users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == email:
                return True
    return False
    
    
# Call the function to create the footer
create_footer()

if __name__ == '__main__':
    main()
    
    
