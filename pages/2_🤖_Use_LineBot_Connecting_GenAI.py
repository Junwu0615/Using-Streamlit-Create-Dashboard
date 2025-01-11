# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-11
"""
import json, time, requests
import numpy as np
import pandas as pd
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

st.markdown('## :rainbow[Use LineBot Connecting GenAI]', unsafe_allow_html=True, help='Beta Testing')
st.image('./source/linebot_qrcode.png', width=200)

@st.cache_data
def get_stat_data():
    gist_url = 'https://gist.github.com/Junwu0615/ca299a80b6f8c17db9067a6c60ea6681'
    res = requests.get(f"{gist_url}/raw")
    if res.status_code in [200, 201]:
        loader = json.loads(res.text)
        chart_data = pd.DataFrame({0: loader})
        return chart_data
    else:
        print(f"Failed to fetch Gist: {res.status_code}")
        return None

chart_data = get_stat_data()
# print(chart_data)

if st.button('Manually Update Data', icon='📊'):
    get_stat_data.clear()
    chart_data = get_stat_data()

if chart_data is not None:
    st.bar_chart(
        chart_data,
        x_label='Count',
        y_label='Statistics Item',
        color=['#b53a3a'],
        width=1000,
        horizontal=True, # 交換x/y軸
        use_container_width=False,
    )

# idx = 0
# chart = st.empty()
# while idx < 5:
#     # 若有多個用戶則可按筆數來動態更新
#     chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
#     chart.bar_chart(chart_data)
#     time.sleep(0.2)
#     idx += 1

st.markdown(
'''
##### :blue-background[Current Application Technologies]
 - **Gen AI** : ~~`Chat GPT`~~ `Google Gemini`
 - **Backend** : `SQL Server` `NGROK` `Flask` `Git Gist` `GitHub` 
 - **Communication Software** : `LineBot`
 - **Programming** : `Python`
<br> 
##### :blue-background[Future Work]
 - **Image Recognition** : `YOLO`
 - **Deploy** : `Docker` `Cloud`
 - **Development** : :red-background[*Human Companion Robot*]
<br> 
''', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ['A. Creator’s GitHub',
     'B. Identify Food and Feedback',
     'C. GIF Meme Name Search',
     'D. Creator’s Dashboard',
     'E. Human Companion Robot',
     'F. Generate Self-Introduction']
)
with tab1:
    # Creator’s GitHub
    st.image('./source/a.gif')

with tab2:
    # Identify Food and Feedback
    st.image('./source/b.gif')

with tab3:
    # GIF Meme Name Search
    st.image('./source/c.gif')

with tab4:
    # Creator’s Dashboard
    st.image('./source/d.gif')

with tab5:
    # Human Companion Robot
    st.image('./source/e.gif')

with tab6:
    # Generate Self-Introduction
    st.image('./source/f.gif')

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