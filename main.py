# streamlit_app.py
import streamlit as st
import subprocess

st.title("Launch Ursina Game")

if st.button("Start Game"):
    subprocess.Popen(["python", "ursina_game.py"])
