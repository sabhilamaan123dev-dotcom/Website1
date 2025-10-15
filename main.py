# streamlit_app.py
import streamlit as st
import random

# CONFIG
TOTAL_LEVELS = 5
JUMPS_PER_LEVEL = 25
SUCCESS_RATE = 0.85  # 85% success rate per jump

# Initialize session state
if "level" not in st.session_state:
    st.session_state.level = 1
    st.session_state.jump = 1
    st.session_state.deaths = 0
    st.session_state.won = False

# Page setup
st.set_page_config(page_title="Parkour Obby", layout="centered")
st.title("🏃‍♂️ Parkour Obby Simulator")
st.markdown(f"Level **{st.session_state.level}** / {TOTAL_LEVELS} &nbsp;&nbsp;|&nbsp;&nbsp; Jump **{st.session_state.jump}** / {JUMPS_PER_LEVEL}")

# Display placeholder image
st.image("https://i.imgur.com/7nYQZ0D.png", width=300)

# Main game logic
if not st.session_state.won:
    if st.button("Jump!"):
        success = random.random() < SUCCESS_RATE
        if success:
            if st.session_state.jump < JUMPS_PER_LEVEL:
                st.session_state.jump += 1
                st.success("✅ You made the jump!")
            else:
                if st.session_state.level < TOTAL_LEVELS:
                    st.session_state.level += 1
                    st.session_state.jump = 1
                    st.balloons()
                    st.success(f"🎉 Level {st.session_state.level - 1} complete! On to level {st.session_state.level}")
                else:
                    st.session_state.won = True
                    st.balloons()
        else:
            st.session_state.deaths += 1
            st.error("💀 You missed the jump! Try again.")

else:
    st.header("🏁 YOU WIN!")
    st.success("You've completed all levels of the Parkour Obby!")
    st.balloons()

    if st.button("Restart Game"):
        st.session_state.level = 1
        st.session_state.jump = 1
        st.session_state.deaths = 0
        st.session_state.won = False

# Sidebar stats
with st.sidebar:
    st.header("📊 Game Stats")
    st.metric("Current Level", st.session_state.level)
    st.metric("Current Jump", st.session_state.jump)
    st.metric("Total Deaths", st.session_state.deaths)
    if st.session_state.won:
        st.success("🏆 Victory Achieved!")
