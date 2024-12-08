import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu

# Using "with" notation
with st.sidebar:
    icon= st.button("Click here 🦊")
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
    selection = option_menu(
                menu_title=None,
                options = ["Accueil", "Photos"])
    if selection == "Accueil":
      st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo 🐱")

image_url = 'https://demo-source.imgix.net/mountains.jpg'
st.image(image_url, caption = "Mountains")

col1, col2, col3 = st.columns(3)

with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")


# Using object notation
# add_selectbox = st.sidebar.selectbox(
    # "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone")