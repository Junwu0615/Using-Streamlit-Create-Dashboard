# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-11
"""
import time
import numpy as np
import pandas as pd
import streamlit as st
from depend.visit_count_logic import visit_count
from settings import LIGHT, DARK, DEFAULT

def stream_data(stream_strings):
    for i in stream_strings.split(' '):
        yield i + ' '
        time.sleep(0.1)

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='PC Dashboard',
    page_icon='🚀️',
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
# 顯示訪客次數
st.markdown(f"""
<img alt="Visit_Count" src="https://img.shields.io/badge/Visit_Count-{visit_count('C2')}-blue&logo=github">
""", unsafe_allow_html=True)

st.write('# 🚀 :rainbow[*A self-evolving data scientist, just like Deep Learning*] 🚀<br>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.75, 2, 0.8]) # 寬度比例
with col1:
    st.image('./source/photo-stickers.jpg', caption='Photo-Stickers From My GitHub')
with col2:
    st.markdown(f'''
    Hi, I'm **Ping Chun Wu** :sunglasses:, a passionate developer with a focus on :blue-background[*Data Science*], :blue-background[*Machine Learning*], and :blue-background[*Software Development*]. 
    I enjoy solving complex problems and continuously learning to improve my skills.
    ''', unsafe_allow_html=True)

    if st.button('[ Click Me ] Professional Growth'):
        text = ('- 2020 Shih Chien University - Information Management ( IM )\n'
                '- 2023 Feng Chia University - Computer Science and Information Engineering ( CSIE )\n'
                '- 2024 Data Scientist ( Hsinchu )\n'
                '- 2025 ? ? ?')
        st.write_stream(stream_data(text))

with col3:
    pass

# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
# for i in range(1, 51):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     chart.add_rows(new_rows)
#     last_rows = new_rows
#     time.sleep(0.05)

st.markdown('<br>', unsafe_allow_html=True)
st.markdown('#### EXPERTISE', unsafe_allow_html=True)
st.markdown(f'''
##### :blue-background[A . Python Skills]
 - **⭐ :rainbow[MASTER] ⭐**
     - Strings ,  List ,  Tuple ,  Dict ,  Set ,  For Loop, Array ,  DataFrame , Class, Inheritance, ... etc.
 - **⭐ :rainbow[FREQUENTLY UTILIZED] ⭐**
    - **Machine Learning :** PyTorch, `TensorFlow`, `Keras`, Scikit-Learn, `NumPy`, `Pandas`, OpenCV
    - **Data Visualization :** `Streamlit`, Plotly, Matplotlib, ... etc.
    - **Web Crawler :** `BeautifulSoup`, `Selenium`
    - **Database :** SQLAlchemy, `pyodbc`
    - **Messaging :** LineBotSDK, WebSocket, ... etc.
    - **Special Tools :** ArgumentParser, ThreadPoolExecutor, setuptools, ... etc.
    - **Base Tools :** os, enum, time, requests, datetime, decimal, copy, json, flask, pickle, datasets, schedule, PIL, rich, tqdm, ... etc.
''', unsafe_allow_html=True)

st.markdown('---')

st.markdown(f'''
##### :blue-background[B . Programming]
 - **Frontend :** HTML / CSS / Markdown
 - **Backend :** `Python` / PHP / C / C++
 - **Database :** `SQL Server` / PostgreSQL / MySQL / SQLite
 - **Version Control :** `GitHub`
 - **Deploy :** `Docker` ( Container / Image / Swarm / Compose )
 - **Messaging :** MQTT / WebSocket / Line / Telegram
 - **Operating System :** Windows / Linux
 - **Other :** WampServer / NGROK / Git-Gist / Git Action / GistHub.io
''', unsafe_allow_html=True)

st.markdown('---')

st.markdown(f'''
##### :blue-background[C . Production Software]
 - **Job Tool :** `ChatGPT` / `Github Copilot` / `Youtrack` / Notion / Google Gemini
 - **Programming Environment :** `PyCharm` / Jupyter / Spyder / VScode / VS
 - **Microsoft Office :** Excel / Word / PowerPoint
 - **Adobe Software :** Photoshop / Premiere / After Effects / Acrobat
''', unsafe_allow_html=True)


st.markdown("""
<style>
.rainbow-animation {
  font-size: 32px;
  font-weight: bold;
  background: linear-gradient(90deg, red, orange, yellow, green, indigo, violet);
  background-size: 400%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: rainbow 5s linear infinite;
}
@keyframes rainbow {
  100% { background-position: 100%; }
  100% { background-position: -200%; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)