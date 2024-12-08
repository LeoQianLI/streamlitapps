import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
st.set_page_config(
    page_title = "Multipage App",
    page_icon = " :wave:",
)
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
  st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés 🎉")
if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  

  from streamlit_option_menu import option_menu

# Using "with" notation
  with st.sidebar:
      authenticator.logout("Déconnexion 🦊")
      #icon= st.button("Click here 🦊")
# Création du menu qui va afficher les choix qui se trouvent dans la variable options
      selection = option_menu(
                 menu_title=None,
                options = ["Accueil 👏", "Photos 	🖼️"])
  if selection == "Accueil 👏":
      st.write("Bienvenue sur la page d'accueil ! 📺")
      image_url = 'https://demo-source.imgix.net/mountains.jpg'
      st.image(image_url, caption = "Mountains")

  elif selection == "Photos 	🖼️":
      st.write("Bienvenue sur mon album photo 🐱")
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

elif st.session_state["authentication_status"] is False:
      st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
      st.warning('Les champs username et mot de passe doivent être remplie')


# Using object notation
# add_selectbox = st.sidebar.selectbox(
    # "How would you like to be contacted?",
    # ("Email", "Home phone", "Mobile phone")