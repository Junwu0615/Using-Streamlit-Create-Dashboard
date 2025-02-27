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
# ?style=flat, social, flat-square, plastic, for-the-badge 更改 style
# ?color=red 更改 Logo 顏色
# ?labelColor=black 更改背景顏色
# ?logoColor=white 更改 label 背景顏色
# ?logo=github  更改 Logo # https://simpleicons.org/
# ?label=YourText 更改 label 名稱
st.markdown(f"""
<img alt="Visit_Count" src="https://img.shields.io/badge/Visit_Count-{visit_count('C2')}-blue?logo=ferrari&style=flat-square">
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

# st.markdown('<br>', unsafe_allow_html=True)
# st.markdown('#### EXPERTISE', unsafe_allow_html=True)
# st.markdown(f'''
# ##### :blue-background[A . Python Skills]
#  - **⭐ :rainbow[MASTER] ⭐**
#      - Strings ,  List ,  Tuple ,  Dict ,  Set ,  For Loop, Array ,  DataFrame , Class, Inheritance, ... etc.
#  - **⭐ :rainbow[FREQUENTLY UTILIZED] ⭐**
#     - **Machine Learning :** PyTorch, `TensorFlow`, `Keras`, Scikit-Learn, `NumPy`, `Pandas`, OpenCV
#     - **Data Visualization :** `Streamlit`, Plotly, Matplotlib, ... etc.
#     - **Web Crawler :** `BeautifulSoup`, `Selenium`
#     - **Database :** SQLAlchemy, `pyodbc`
#     - **Messaging :** LineBotSDK, WebSocket, ... etc.
#     - **Special Tools :** ArgumentParser, ThreadPoolExecutor, setuptools, ... etc.
#     - **Base Tools :** os, enum, time, requests, datetime, decimal, copy, json, flask, pickle, datasets, schedule, PIL, rich, tqdm, ... etc.
# ''', unsafe_allow_html=True)
#
# st.markdown('---')
#
# st.markdown(f'''
# ##### :blue-background[B . Programming]
#  - **Frontend :** HTML / CSS / Markdown
#  - **Backend :** `Python` / PHP / C / C++
#  - **Database :** `SQL Server` / PostgreSQL / MySQL / SQLite
#  - **Version Control :** `GitHub`
#  - **Deploy :** `Docker` ( Container / Image / Swarm / Compose )
#  - **Messaging :** MQTT / WebSocket / Line / Telegram
#  - **Operating System :** Windows / Linux
#  - **Other :** WampServer / NGROK / Git-Gist / Git Action / GistHub.io
# ''', unsafe_allow_html=True)
#
# st.markdown('---')
#
# st.markdown(f'''
# ##### :blue-background[C . Production Software]
#  - **Job Tool :** `ChatGPT` / `Github Copilot` / `Youtrack` / Notion / Google Gemini
#  - **Programming Environment :** `PyCharm` / Jupyter / Spyder / VScode / VS
#  - **Microsoft Office :** Excel / Word / PowerPoint
#  - **Adobe Software :** Photoshop / Premiere / After Effects / Acrobat
# ''', unsafe_allow_html=True)

st.markdown('---')
st.markdown(f'''
<!-- Languages -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Languages </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://www.python.org/">
                        <img alt="Python" width="50" height="50" src="https://techstack-generator.vercel.app/python-icon.svg"/>
                    </a>
                    <br> Python
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.w3schools.com/c/c_intro.php">
                        <img alt="C" width="40" height="50" src="https://skillicons.dev/icons?i=c"/>
                    </a>
                    <br> C
                </td>
                <td align="center" style="border: none;">
                    <a href="https://zh.wikipedia.org/zh-tw/C%2B%2B">
                        <img alt="CPP" width="40" height="50" src="https://skillicons.dev/icons?i=cpp"/>
                    </a>
                    <br> C++
                </td>
                <td align="center" style="border: none;">
                    <a href="https://developer.mozilla.org/zh-TW/docs/Web/HTML">
                        <img alt="HTML" width="40" height="50" src="https://skillicons.dev/icons?i=html"/>
                    </a>
                    <br> HTML
                </td>
                <td align="center" style="border: none;">
                    <a href="https://developer.mozilla.org/zh-TW/docs/Web/CSS">
                        <img alt="CSS" width="40" height="50" src="https://skillicons.dev/icons?i=css"/>
                    </a>
                    <br> CSS
                </td>
                <td align="center" style="border: none;">
                    <a href="https://markdown.tw/">
                        <img alt="Markdown" width="45" height="50" src="https://skillicons.dev/icons?i=md"/>
                    </a>
                    <br> Markdown
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.php.net/">
                        <img alt="PHP" width="50" height="50" src="https://skillicons.dev/icons?i=php"/>
                    </a>
                    <br> PHP
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Database -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Database </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icons/set/sql-server">
                        <img alt="SQL Server" width="50px" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/sql-server.png"/>
                    </a>
                    <br> SQL Server
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.postgresql.org/">
                        <img alt="PostgreSQL" width="50" height="50" src="https://skillicons.dev/icons?i=postgresql"/>
                    </a>
                    <br> PostgreSQL
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.mysql.com/">
                        <img alt="MySQL" width="50" height="50" src="https://techstack-generator.vercel.app/mysql-icon.svg"/>
                    </a>
                    <br> MySQL
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icons/set/sqlite">
                        <img alt="SQLite" width="50px" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/sqlite.png"/>
                    </a>
                    <br> SQLite
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- LLM & Machine Learning -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> LLM & Machine Learning </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://chatgpt.com/" style="color: white;">
                        <img alt="ChatGPT" width="40" height="50" src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg"/>
                    </a>
                    <br> ChatGPT
                </td>
                <td align="center" style="border: none;">
                    <a href="https://gemini.google.com/?hl=zh-TW" style="color: white;">
                        <img alt="Google Gemini" width="75" height="65" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/Gemini.gif"/>
                    </a>
                    <br> Google Gemini
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.tensorflow.org/">
                        <img alt="Tensorflow" width="70" height="70" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/Tensorflow.gif"/>
                    </a>
                    <br> Tensorflow
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/z2pN6mJXIC4u/keras">
                        <img alt="Keras" width="50px" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/Keras.png"/>
                    </a>
                    <br> Keras
                </td>
                <td align="center" style="border: none;">
                    <a href="https://pytorch.org/">
                        <img alt="PyTorch" width="40" height="50" src="https://skillicons.dev/icons?i=pytorch"/>
                    </a>
                    <br> PyTorch
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Deploy & Cloud -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Deploy & Cloud </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://www.docker.com/">
                        <img alt="Docker" width="50" height="50" src="https://techstack-generator.vercel.app/docker-icon.svg"/>
                    </a>
                    <br> Docker
                </td>
                <td align="center" style="border: none;">
                    <a href="https://aws.amazon.com" style="color: white;">
                        <img alt="AWS" width="40" height="50" src="https://techstack-generator.vercel.app/aws-icon.svg"/>
                    </a>
                    <br> AWS
                </td>
                <td align="center" style="border: none;">
                    <a href="https://azure.microsoft.com/zh-tw" style="color: white;">
                        <img alt="Azure" width="40" height="50" src="https://skillicons.dev/icons?i=azure"/>
                    </a>
                    <br> Azure
                </td>
                <td align="center" style="border: none;">
                    <a href="https://cloud.google.com" style="color: white;">
                        <img alt="GCP" width="40" height="50" src="https://skillicons.dev/icons?i=gcp"/>
                    </a>
                    <br> GCP
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Skills -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Skills </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://numpy.org/">
                        <img alt="NumPy" width="40" height="50" src="https://cdn.worldvectorlogo.com/logos/numpy-1.svg"/>
                    </a>
                    <br> NumPy
                </td>
                <td align="center" style="border: none;">
                    <a href="https://pandas.pydata.org/">
                        <img alt="Pandas" width="80" height="50" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/pandas.svg"/>
                    </a>
                    <br> Pandas
                </td>
                <td align="center" style="border: none;">
                    <a href="https://flask.palletsprojects.com/">
                        <img alt="Flask" width="40" height="50" src="https://skillicons.dev/icons?i=flask"/>
                    </a>
                    <br> Flask
                </td>
                <td align="center" style="border: none;">
                    <a href="https://fastapi.tiangolo.com/">
                        <img alt="FastAPI" width="40" height="50" src="https://skillicons.dev/icons?i=fastapi"/>
                    </a>
                    <br> FastAPI
                </td>
                <td align="center" style="border: none;">
                    <a href="https://ngrok.com/">
                        <img alt="NGROK" width="45" height="45" src="https://avatars.githubusercontent.com/u/10625446?s=280&v=4"/>
                    </a>
                    <br> NGROK
                </td>
            </tr>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://github.com/features/actions">
                        <img alt="Github Actions" width="40" height="50" src="https://skillicons.dev/icons?i=githubactions"/>
                    </a>
                    <br> Github Actions
                </td>
                <td align="center" style="border: none;">
                    <a href="https://gist.github.com/">
                        <img alt="Github Gist" width="50" height="50" src="https://k9982874.gallerycdn.vsassets.io/extensions/k9982874/github-gist-explorer/0.2.3/1638842316475/Microsoft.VisualStudio.Services.Icons.Default"/>
                    </a>
                    <br> Github Gist
                </td>
                <td align="center" style="border: none;">
                    <a href="https://airflow.apache.org/">
                        <img alt="Apache Airflow" width="40" height="40" src="https://airflow.apache.org/docs/apache-airflow/1.10.15/_images/pin_large.png"/>
                    </a>
                    <br> Apache Airflow
                </td>
                <td align="center" style="border: none;">
                    <a href="https://streamlit.io/">
                        <img alt="Streamlit" width="40" height="40" src="https://raw.githubusercontent.com/rlew631/rlew631/5fcb1cee69c8034bfa2b98aad94b584fcff8d84f/streamlit_red.svg"/>
                    </a>
                    <br> Streamlit
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.wampserver.com/en/">
                        <img alt="WampServer" width="40" height="40" src="https://www.bugtreat.com/blog/wp-content/uploads/2012/07/WampServer-logo.png"/>
                    </a>
                    <br> WampServer
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Message & Version Control -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="4" align="center"> Message </th>
                <th colspan="2" align="center"> Version Control </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://web.telegram.org/">
                        <img alt="Telegram" width="40" height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1200px-Telegram_logo.svg.png"/>
                    </a>
                    <br> Telegram
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.line.me/tw/">
                        <img alt="Line" width="40" height="40" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/LINE_logo.svg/1024px-LINE_logo.svg.png"/>
                    </a>
                    <br> Line
                </td>
                <td align="center" style="border: none;">
                    <a href="https://aws.amazon.com/tw/what-is/mqtt/">
                        <img alt="MQTT" width="40" height="40" src="https://avatars.githubusercontent.com/u/1544528?s=280&v=4"/>
                    </a>
                    <br> MQTT
                </td>
                <td align="center" style="border: none;">
                    <a href="https://developer.mozilla.org/zh-TW/docs/Web/API/WebSocket">
                        <img alt="WebSocket" width="40" height="35" src="https://blog.gtwang.org/wp-content/uploads/2015/03/websocket-logo.png"/>
                    </a>
                    <br> WebSocket
                </td>
                <td align="center" style="border: none;">
                    <a href="https://github.com/">
                        <img alt="Git" width="40" height="50" src="https://skillicons.dev/icons?i=git"/>
                    </a>
                    <br> Git
                </td>
                <td align="center" style="border: none;">
                    <a href="https://github.com/">
                        <img alt="Github" width="50" height="50" src="https://techstack-generator.vercel.app/github-icon.svg"/>
                    </a>
                    <br> Github
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- IDE of Programming -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> IDE of Programming </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://www.jetbrains.com/pycharm/">
                        <img alt="PyCharm" width="50" height="50" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/pycharm.gif" />
                    </a>
                    <br> PyCharm
                </td>
                <td align="center" style="border: none;">
                    <a>
                        <img alt="Azure Data Studio" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/azure_data_studio.png"/>
                    </a>
                    <br> Azure Data Studio
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/F4uMFPZgS0gt/anaconda">
                        <img alt="Anaconda" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/anaconda.png"/>
                    </a>
                    <br> Anaconda
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icons/set/jupyter">
                        <img alt="Jupyter" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/jupyter.png"/>
                    </a>
                    <br> Jupyter
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/0S1Hoidfnk7H/spyder-ide-5">
                        <img alt="Spyder" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/spyder.png"/>
                    </a>
                    <br> Spyder
                </td>
                <td align="center" style="border: none;">
                    <a href="https://code.visualstudio.com/">
                        <img alt="VS Code" width="45" height="50" src="https://skillicons.dev/icons?i=vscode"/>
                    </a>
                    <br> VS Code
                </td>
                <td align="center" style="border: none;">
                    <a href="https://visualstudio.microsoft.com/zh-hant/downloads/">
                        <img alt="VS" width="45" height="50" src="https://skillicons.dev/icons?i=visualstudio"/>
                    </a>
                    <br> VS
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Operating System & Job Tools -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="3" align="center"> Operating System </th>
                <th colspan="2" align="center"> Command Tools </th>
                <th colspan="4" align="center"> Job Tools </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://www.microsoft.com/zh-tw/software-download/windows10">
                        <img alt="Windows" width="40" height="50" src="https://skillicons.dev/icons?i=windows"/>
                    </a>
                    <br> Windows
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.linux.org/">
                        <img alt="Linux" width="40" height="50" src="https://skillicons.dev/icons?i=linux"/>
                    </a>
                    <br> Linux
                </td>
                <td align="center" style="border: none;">
                    <a href="https://ubuntu.com/download">
                        <img alt="Ubuntu" width="70" height="50" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/ubuntu.gif" />
                    </a>
                    <br> Ubuntu
                </td>
                <td align="center" style="border: none;">
                    <a href="https://learn.microsoft.com/zh-tw/powershell/scripting/overview?view=powershell-7.5">
                        <img alt="Powershell" width="45" height="50" src="https://skillicons.dev/icons?i=powershell"/>
                    </a>
                    <br> Powershell
                </td>
                <td align="center" style="border: none;">
                    <a href="https://learn.microsoft.com/zh-tw/windows-server/administration/windows-commands/cmd">
                        <img alt="CMD" width="45" height="45" src="https://devblogs.microsoft.com/commandline/wp-content/uploads/sites/33/2019/03/CommandLineIcon.png"/>
                    </a>
                    <br> CMD
                </td>
                <td align="center" style="border: none;">
                    <a>
                        <img alt="Copilot" width="45" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/github_copilot.png"/>
                    </a>
                    <br> Copilot
                </td>
                <td align="center" style="border: none;">
                    <a>
                        <img alt="Youtrack" width="45" height="45" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/youtrack.png"/>
                    </a>
                    <br> Youtrack
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/set/notion/group-ui">
                        <img alt="Notion" width="45" height="45" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/notion.png"/>
                    </a>
                    <br> Notion
                </td>
                <td align="center" style="border: none;">
                    <a href="https://jmeter.apache.org/">
                        <img alt="Apache JMeter" width="110" height="45" src="https://jmeter.apache.org/images/jmeter.png"/>
                    </a>
                    <br> Apache JMeter
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Base Tools -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Base Tools </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/rZObyIJRui2T/adobe-acrobat">
                        <img alt="Adobe Acrobat" width="45" height="45" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/acrobat.png"/>
                    </a>
                    <br> Acrobat
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.adobe.com/tw/products/photoshop.html">
                        <img alt="Adobe Photoshop" width="40" height="50" src="https://cdn.worldvectorlogo.com/logos/adobe-photoshop-2.svg"/>
                    </a>
                    <br> PS
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.adobe.com/tw/products/premiere.html">
                        <img alt="Adobe Premiere Pro" width="40" height="50" src="https://upload.wikimedia.org/wikipedia/commons/4/40/Adobe_Premiere_Pro_CC_icon.svg"/>
                    </a>
                    <br> PR
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.adobe.com/tw/products/aftereffects.html">
                        <img alt="Adobe After Effects" width="40" height="50" src="https://cdn.worldvectorlogo.com/logos/after-effects-1.svg"/>
                    </a>
                    <br> AE
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/117563/microsoft-word-2019">
                        <img alt="Word" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/word.png"/>
                    </a>
                    <br> Word
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/ifP93G7BXUhU/microsoft-powerpoint-2019">
                        <img alt="PowerPoint" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/ppt.png"/>
                    </a>
                    <br> PowerPoint
                </td>
                <td align="center" style="border: none;">
                    <a href="https://icons8.com/icon/117561/microsoft-excel-2019">
                        <img alt="Excel" width="40" height="40" src="https://raw.githubusercontent.com/Junwu0615/Junwu0615/main/icon/excel.png"/>
                    </a>
                    <br> Excel
                </td>
            </tr>
        </tbody>
    </table>
</div>

<!-- Studying -->
<div align="center">
    <table>
        <thead>
            <tr>
                <th colspan="10" align="center"> Studying </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="center" style="border: none;">
                    <a href="https://reactjs.org/" style="color: white;">
                        <img alt="React" width="40" height="50" src="https://techstack-generator.vercel.app/react-icon.svg"/>
                    </a>
                    <br> React
                </td>
                <td align="center" style="border: none;">
                    <a href="https://developer.mozilla.org/zh-TW/docs/Web/JavaScript" style="color: white;">
                        <img alt="JavaScript" width="40" height="50" src="https://techstack-generator.vercel.app/js-icon.svg"/>
                    </a>
                    <br> JavaScript
                </td>
                <td align="center" style="border: none;">
                    <a href="https://www.djangoproject.com/" style="color: white;">
                        <img alt="Django" width="40" height="50" src="https://techstack-generator.vercel.app/django-icon.svg"/>
                    </a>
                    <br> Django
                </td>
                <td align="center" style="border: none;">
                    <a href="https://grafana.com/" style="color: white;">
                        <img alt="Grafana" width="40" height="50" src="https://skillicons.dev/icons?i=grafana"/>
                    </a>
                    <br> Grafana
                </td>
                <td align="center" style="border: none;">
                    <a href="https://kubernetes.io/" style="color: white;">
                        <img alt="Kubernetes" width="40" height="50" src="https://techstack-generator.vercel.app/kubernetes-icon.svg"/>
                    </a>
                    <br> Kubernetes
                </td>
            </tr>
        </tbody>
    </table>
</div>

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