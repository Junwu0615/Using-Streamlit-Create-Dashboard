# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import os, time, shutil
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

def stream_data(stream_strings):
    for i in stream_strings.split(' '):
        yield i + ' '
        time.sleep(0.1)

if 'theme_mode' not in st.session_state:
    st.session_state['theme_mode'] = 'Dark Mode'

st.set_page_config(
    page_title='PC Dashboard',
    page_icon='🚀️',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

theme_mode = st.sidebar.radio(
    'Select Theme Mode :', ('Light Mode', 'Dark Mode'),
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

st.write('## 🚀 :rainbow[A self-evolving data scientist, just like Deep Learning] 🚀<br>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.75, 2, 0.8]) # 寬度比例
with col1:
    st.image('./source/photo-stickers.jpg', caption='Photo-Stickers From My GitHub')
with col2:
    st.markdown(f'''
    Hi, I'm **Ping Chun Wu** :sunglasses:, a passionate developer with a focus on :blue-background[Data Science], :blue-background[Machine Learning], and :blue-background[Software Development]. 
    I enjoy solving complex problems and continuously learning to improve my skills.
    ''', unsafe_allow_html=True)

    if st.button('[ Click Me ] The Growth Experience'):
        text = ('- 2020 USC IM\n'
                '- 2023 FCU IE\n'
                '- 2024 Data Scientist\n'
                '- 2025 ???')
        st.write_stream(stream_data(text))

with col3:
    pass

st.markdown('<br>', unsafe_allow_html=True)
st.markdown('#### EXPERTISE', unsafe_allow_html=True)
st.markdown(f'''
##### :blue-background[A.]　Python Skills
 - **⭐ :rainbow[MASTER] ⭐**
     - [ Strings ], [ List ], [ Tuple ], [ Dict ], [ Set ], [ For Loop ], 
     <br>[ Array ], [ DataFrame ], `[ Class ]`, `[ Inheritance ]`, ... etc.
 - **⭐ :rainbow[FREQUENTLY UTILIZED] ⭐**
    - **Machine Learning :** PyTorch, `TensorFlow`, `Keras`, Scikit-Learn, `NumPy`, `Pandas`, OpenCV
    - **Data Visualization :** Plotly, Matplotlib, Streamlit, rich, tqdm, ... etc.
    - **Web Crawler :** `BeautifulSoup`, `Selenium`
    - **Database :** SQLAlchemy, `pyodbc`
    - **Special Tools :** ArgumentParser, ThreadPoolExecutor, setuptools, ... etc.
    - **Messaging :** LineBotSDK, WebSocket, ... etc.
    - **Base Tools :** os, enum, time, requests, datetime, decimal, copy, json, flask, pickle, datasets, schedule, PIL, ... etc.
''', unsafe_allow_html=True)

st.markdown('---')

st.markdown(f'''
##### :blue-background[B.]　Programming
 - **Frontend :** HTML / CSS / Markdown
 - **Backend :** `Python` / PHP / C / C++
 - **DataBase :** `SQL Server`
 - **Version Control :** `GitHub`
 - **Deploy :** `Docker`
 - **Messaging :** MQTT / WebSocket / Line / Telegram
 - **Operating System :** Windows / Linux
 - **Other :** WampServer / NGROK / Git-Gist / Git Action / GistHub.io
''', unsafe_allow_html=True)

st.markdown('---')

st.markdown(f'''
##### :blue-background[C.]　Production Software
 - **Job Tool :** `ChatGPT` / `Github Copilot` / `Youtrack` / Notion
 - **Programming Environment :** `PyCharm` / Jupyter / Spyder / VScode / VS
 - **Microsoft Office :** Excel / Word / PowerPoint
 - **Adobe Software :** Photoshop / Premiere / After Effects / Acrobat
''', unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)