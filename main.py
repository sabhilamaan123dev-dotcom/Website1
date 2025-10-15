import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🎮 3D Obby Game (Three.js + Streamlit)")

st.markdown("Click below to play the game right inside the app!")

# Load the local HTML file containing the game
with open("index.html", "r", encoding="utf-8") as f:
    game_html = f.read()

components.html(game_html, height=650, scrolling=False)
