import streamlit as st
def fancy_header(text, font_size=47):
    res = f'<span style="color:#3030FF; font-size: {font_size}px;"><b>{text}</b></span>'
    st.markdown(res, unsafe_allow_html=True )
    



fancy_header('COMING SOON!...🚧')