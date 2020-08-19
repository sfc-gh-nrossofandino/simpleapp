import streamlit as st
import logging

st.title("Test App!!!")

log_text = st.text_input('Log text:')
if st.button("send log"):
    logging.info(log_text)
