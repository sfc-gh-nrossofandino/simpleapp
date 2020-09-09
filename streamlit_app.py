import streamlit as st
import logging

# Create a logger object.
#logger = logging.getLogger(__name__)

# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.
#coloredlogs.install(level='DEBUG')

# If you don't want to see log messages from libraries, you can pass a
# specific logger object to the install() function. In this case only log
# messages originating from that logger will show up on the terminal.
#coloredlogs.install(level='DEBUG', logger=logger)

st.title("Test App!!!")

log_text = st.text_input('Log text:')
if st.button("send log"):
    logging.info(log_text)


st.write(st.experimental_get_query_params())


query_param = st.text_input("query param:")
if st.button('set query param'):
    st.experimental_set_query_params(test=query_param)
