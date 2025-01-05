# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='Use LineBot Connecting GenA',
    page_icon='🤖',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

# on = st.toggle('Theme Mode', value=st.session_state.theme_mode, help='Light Mode / Dark Mode')
# if on:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True
#     st.session_state['df_color'] = 'DarkRed'
# else:
#     shutil.copy2(LIGHT, DEFAULT)
#     st.session_state['theme_mode'] = False
#     st.session_state['df_color'] = 'LightSteelBlue'

# --------- content --------- #

st.markdown('## :rainbow[Use LineBot Connecting GenAI]', unsafe_allow_html=True, help='This service is temporarily closed.')
st.image('./source/linebot_qrcode.png', width=200)
st.markdown(
'''
#### Technologies include the following
 - **Gen AI** : :blue-background[Chat GPT]
 - **Image Recognition** : :blue-background[YOLO]
 - **Communication Software** : :blue-background[LineBot]
 - **Programming** : :blue-background[Python]
<br> 
''', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ['Creator’s GitHub',
     'Creator’s Dashboard',
     'GIF Meme Name Search',
     'Identify Food and Feedback',
     'Human Companion Robot',
     'Generate Self-Introduction']
)
with tab1:
    # Creator’s GitHub
    st.markdown("### Linking to PC's GitHub<br>", unsafe_allow_html=True)
    st.image('./source/github.jpg', width=800)
with tab2:
    # Creator’s Dashboard
    st.markdown("### Linking to PC's Dashboard<br>", unsafe_allow_html=True)
    st.image('./source/dashboard.jpg', width=800)
with tab3:
    # GIF Meme Name Search
    st.markdown("### Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab4:
    # Identify Food and Feedback
    st.markdown("### Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab5:
    # Human Companion Robot
    st.markdown("### Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)
with tab6:
    # Generate Self-Introduction
    st.markdown("### Coming Soon ...<br>", unsafe_allow_html=True)
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)

css = '''
<style>
    .stTabs [data-baseweb='tab-list'] button [data-testid='stMarkdownContainer'] p {
    font-size:1rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)