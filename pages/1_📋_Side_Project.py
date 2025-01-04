# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import streamlit as st

st.set_page_config(
    page_title='Side Project',
    page_icon='📋',
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown('## Side Project')

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


col1, col2 = st.columns([1, 2])  # 左欄寬度1，右欄寬度2
with col1:
    st.image("./source/photo-stickers.jpg")
with col2:
    st.markdown("""
    ## About Me  
    Hi, I'm **Ping Chun Wu**, a passionate developer with expertise in:  
    - Data Science  
    - Machine Learning  
    - Software Development  
    """)
