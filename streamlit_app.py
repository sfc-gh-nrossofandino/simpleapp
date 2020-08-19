import streamlit as st
import logging

st.title("Test App!!!")

if st.button("send log"):
    logging.info('sending log')
