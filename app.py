import streamlit as st
import pandas as pd

st.set_page_config(page_title="My First Streamlit App", page_icon="🎈")

st.title("🎈 My First Streamlit App")
st.write(
    """
    This little app lets you:
    1. Enter your name 📛  
    2. Pick a number 🔢  
    3. See a tiny chart 📈
    """
)

# ---- User inputs ----
name = st.text_input("Your name", "Student")
number = st.slider("Pick a number", 1, 10, 5)

st.success(f"Hello, **{name}**! You picked **{number}**.")

# ---- Simple derived data & chart ----
data = pd.DataFrame({"x": list(range(1, number + 1))})
data["square"] = data["x"] ** 2

st.subheader("Squares up to your number")
st.bar_chart(data.set_index("x"))

st.caption("Made with ❤️ and Streamlit")
