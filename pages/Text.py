import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

def process_text(text):
    url = "https://webhook.site/1eda8b10-2f28-43cd-94ab-e99db2bb3109"
    myobj = {'text': text}

    response = requests.post(url, json = myobj)
    return response

def hover_event(event):
    global highlight_index
    if event.inaxes == ax:
        highlight_index = np.argmax(sizes)
    else:
        highlight_index = -1
    update_pie_chart(highlight_index)

# Highlight the slice on hover
def update_pie_chart(index):
    for i, wedge in enumerate(wedges):
        if i == index:
            wedge.set_alpha(0.8)
        else:
            wedge.set_alpha(1.0)
    fig.canvas.draw()

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
    process_text(text)
    # st.write(process_text(text))
    

    # Define the data
    labels = ['A', 'B', 'C']
    sizes = [20, 10, 35]
    colors = ['#FF595E', '#FFCA3A', '#8AC926']  # Custom colors for the chart

    # Find the index of the largest value
    highlight_index = np.argmax(sizes)

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    explode = [0.1 if i == highlight_index else 0 for i in range(len(labels))]  # Add explosion effect to the highlighted slice
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                    autopct='%1.1f%%', startangle=90, shadow=True)

    # Set the chart title
    ax.set_title('Results')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Customizing text properties
    for text in texts:
        text.set_color('white')
        text.set_fontsize(12)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    # Add interactivity to highlight slices on hover
    highlight_index = -1  # Variable to store the index of highlighted slice



    fig.canvas.mpl_connect('motion_notify_event', hover_event)



    # Display the chart using Streamlit
    st.pyplot(fig)

    # Show the highlighted slice percentage on Streamlit sidebar
    if highlight_index >= 0:
        st.sidebar.markdown(f"**{labels[highlight_index]}**: {sizes[highlight_index]}%")

# Call the function to create the footer
create_footer()
