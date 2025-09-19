import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Say Hello"):
    st.write(f"Hello, {name}! 👋 Welcome to Streamlit!")


st.subheader("Random Data Chart")
data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['X', 'Y']
)
st.line_chart(data)
