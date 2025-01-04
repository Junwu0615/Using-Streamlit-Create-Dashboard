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
    page_title='Steam Discounts Items',
    page_icon='🎮',
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

st.markdown('## Steam Discounts Items<br>', unsafe_allow_html=True)
st.markdown(
    '''
    # Coming Soon ...
    '''
)