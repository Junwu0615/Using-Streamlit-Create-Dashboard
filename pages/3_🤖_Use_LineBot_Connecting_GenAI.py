# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-11
"""
import json, time, requests
import numpy as np
import pandas as pd
import streamlit as st
from base64 import b64encode
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

@st.cache_data
def get_stat_data():
    gist_url = 'https://gist.github.com/Junwu0615/e57debac07e2224f7a7cf794da0aa2ae'
    res = requests.get(f"{gist_url}/raw")
    if res.status_code in [200, 201]:
        loader = json.loads(res.text)
        del loader['text count']
        del loader['media count']
        chart_data = pd.DataFrame({0: loader})
        return chart_data
    else:
        print(f"Failed to fetch Gist: {res.status_code}")
        return None

st.markdown('## :rainbow[Use LineBot Connecting GenAI]', unsafe_allow_html=True, help='Beta Testing')

chart_data = get_stat_data()
# print(chart_data)

col1, col2, col3 = st.columns([0.6, 2, 0.8]) # 寬度比例
with col1:
    # st.image('./source/linebot_qrcode.png', width=200)
    with open("./source/linebot_qrcode.png", "rb") as img_file:
        img_data = b64encode(img_file.read()).decode()
    st.markdown(
    f"""
    <a href="https://line.me/R/ti/p/@059dtndx" target="_blank">
        <img src="data:image/png;base64,{img_data}" alt="QR Code" width="200">
    </a>
    """, unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)

    if st.button('Manually Update Data', icon='📊'):
        get_stat_data.clear()
        chart_data = get_stat_data()

with col2:
    st.markdown('<br>', unsafe_allow_html=True)
    if chart_data is not None:
        st.bar_chart(
            chart_data,
            x_label='Count',
            # y_label='Statistics Item',
            color=['#b53a3a'],
            width=1000,
            horizontal=True,  # 交換x/y軸
            use_container_width=False,
        )

with col3:
    pass

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
##### :blue-background[⭐ Application Technologies]
 - **Gen AI** : ![Chat_GPT](https://img.shields.io/badge/Chat_GPT-412991.svg?logo=openai&logoColor=white) ![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2.svg?logo=googlegemini&logoColor=white)
 - **Backend** :  ![Flask](https://img.shields.io/badge/Flask-000.svg?logo=flask&logoColor=white) ![NGROK](https://img.shields.io/badge/NGROK-1F1E37.svg?logo=ngrok&logoColor=white) ![Git Gist](https://img.shields.io/badge/Git_Gist-F05032.svg?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717.svg?logo=github&logoColor=white) ![SQL_Server](https://img.shields.io/badge/SQL_Server-646565.svg?logo=data:image/jpeg;base64,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)
 - **Communication Software** : ![Line](https://img.shields.io/badge/Line-00c300.svg?logo=line&logoColor=white)
 - **Programming** : ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white)
<br> 
##### :blue-background[⭐ Future Works]
 - **Image Recognition** : `YOLO`
 - **Deploy** : ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=docker&logoColor=white) ![Amazon Web Services](https://img.shields.io/badge/Amazon_Web_Services-232F3E.svg?logo=amazonwebservices&logoColor=white)
 - **Development** : `Human Companion Robot`
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