# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import os, shutil
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

if 'theme_mode' not in st.session_state:
    st.session_state['theme_mode'] = 'Dark Mode'

st.set_page_config(
    page_title='Use LineBot Connecting GenA',
    page_icon='💬',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

theme_mode = st.sidebar.radio(
    'Select Theme Mode:', ('Light Mode', 'Dark Mode'),
    index=0 if st.session_state['theme_mode'] == 'Light Mode' else 1
)
try:
    if theme_mode != st.session_state['theme_mode']:
        st.session_state['theme_mode'] = theme_mode
        match theme_mode:
            case 'Dark Mode':
                shutil.copy2(DARK, DEFAULT)
            case 'Light Mode':
                shutil.copy2(LIGHT, DEFAULT)
        st.rerun()
except Exception as e:
    st.error(f'Failed to {e}')

# --------- content --------- #

st.markdown('## Use LineBot Connecting GenA')
st.image('./source/linebot_qrcode.png', width=200)
st.markdown(
'''
#### Technologies include the following
 - **Gen AI** : `Chat GPT`
 - **Image Recognition** : `YOLO`
 - **Communication Software** : `LineBot`
<br> 
''', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ['創作者 GitHub 頁面', '創作者 Dashboard', 'GIF 梗圖名稱搜索', '識別食物分析營養', '男(女)朋友機器人', '基於履歷生成自我介紹']
)
with tab1:
    st.markdown("## Linking to PC's GitHub<br>", unsafe_allow_html=True)
    st.image('./source/github.jpg', width=800)
with tab2:
    st.markdown("## Linking to PC's Dashboard<br>", unsafe_allow_html=True)
    st.image('./source/dashboard.jpg', width=800)
with tab3:
    st.markdown("## Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab4:
    st.markdown("## Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab5:
    st.markdown("## Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab6:
    st.markdown("## Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)