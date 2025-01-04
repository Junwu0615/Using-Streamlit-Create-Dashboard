# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import shutil
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

st.set_page_config(
    page_title='PC Dashboard',
    page_icon='🚀️',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')
theme_mode = st.sidebar.radio("Select Theme Mode:", ("Light Mode", "Dark Mode"))
shutil.copy(DARK, DEFAULT) if theme_mode == "Light Mode" else shutil.copy(LIGHT, DEFAULT)

st.write('## A self-evolving data scientist, just like deep learning. 🚀')
st.markdown('#')

col1, col2, col3 = st.columns([1, 2, 1])  # 左欄寬度1，右欄寬度2
with col1:
    st.image('./source/photo-stickers.jpg', caption='Photo-Stickers From My GitHub')
with col2:
    st.markdown(f'''
    Hi, I'm **Ping Chun Wu**, a passionate developer with a focus on `Data Science`, `Machine Learning`, and `Software Development`. 
    I enjoy solving complex problems and continuously learning to improve my skills.
    ''', unsafe_allow_html=True)
with col3:
    # st.image('./source/PC.jpg', caption='My Photo')
    pass

st.markdown('---')

st.markdown('### Expertise')
st.markdown(f'''
##### A.　Python Skills
 - **Master**
     - [ Strings ], [ List ], [ Tuple ], [ Dict ], [ Set ], [ For Loop ], 
     <br>[ Array ], [ DataFrame ], `[ Class ]`, `[ Inheritance ]`, ... etc.
 - **Frequently Utilized**
    - **Machine Learning :** PyTorch, `TensorFlow`, `Keras`, Scikit-Learn, `NumPy`, `Pandas`, OpenCV
    - **Data Visualization :** Plotly, Matplotlib, Streamlit, rich, tqdm, ... etc.
    - **Web Crawler :** `BeautifulSoup`, `Selenium`
    - **Database :** SQLAlchemy, `pyodbc`
    - **Special tools :** ArgumentParser, ThreadPoolExecutor, setuptools, ... etc.
    - **Messaging :** LineBotSDK, WebSocket, ... etc.
    - **Base Tool :** os, enum, time, requests, datetime, decimal, copy, json, flask, pickle, datasets, schedule, PIL, ... etc.
''', unsafe_allow_html=True)

st.markdown('---')

st.markdown(f'''
##### B.　Programming
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
##### C.　Production Software
 - **Job Tool :** `ChatGPT` / `Github Copilot` / `Youtrack` / Notion
 - **Programming Environment :** `PyCharm` / Jupyter / Spyder / VScode / VS
 - **Microsoft Office :** Excel / Word / PowerPoint
 - **Adobe Software :** Photoshop / Premiere / After Effects / Acrobat
''', unsafe_allow_html=True)