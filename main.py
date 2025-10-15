import streamlit as st
st.write("Amaan's Gaming Website")
import streamlit as st
import subprocess

st.title("Ammaan's Roblox Website")

if st.button("Run EXE"):
    try:
        # Run the executable
        result = subprocess.run(
            ["./my_program.exe"],  # Or full path if it's elsewhere
            capture_output=True,
            text=True
        )

        # Show output and errors
        st.text("STDOUT:\n" + result.stdout)
        if result.stderr:
            st.text("STDERR:\n" + result.stderr)

