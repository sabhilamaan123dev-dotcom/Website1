import streamlit as st

st.title("🎮 My 3D Obby Game")

st.markdown("Click below to play:")

# Link to local or hosted index.html
game_url = "index.html"  # or http://localhost:8000 if serving

st.markdown(f"[▶️ Play Obby Game]({game_url})", unsafe_allow_html=True)
