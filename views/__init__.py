import streamlit as st
from pages import page1, page2
# --- page setup ---
about_page = st.Page(
    page = page1.py,
    title = "Bienvenue",
    icon = ":film_frames:",
    default = True,
)

page_1 = st.Page(
    page = page2.py,
  
    icon = ":movie_camera:",
)

pg = st.navigation(pages = [about_page, page_1])

pg.run