import streamlit as st
import numpy as np

# show images
# ===========

cols = st.beta_columns(3)
for col, img in zip(cols, np.zeros((3, 250, 250, 3))):
    col.image(img, use_column_width=True)

# show form
# =========

st.text_input("Search term", value="streamlit")

col1, col2 = st.beta_columns([2, 1])
col1.selectbox("1 month ago", options=["A", "B"])
col2.number_input("Limit", value=10000)

col3, col4, col5 = st.beta_columns(3)
col3.number_input("Minimum replies", value=0)
col4.number_input("Minimum retweets", value=0)
col5.number_input("Minimum hearts", value=0)
