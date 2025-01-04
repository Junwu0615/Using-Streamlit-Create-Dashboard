# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-04
"""
import streamlit as st

st.set_page_config(
    page_title='PC Dashboard',
    page_icon='🚀️',
)

st.write('## A self-evolving data scientist, just like deep learning. 🚀')
st.sidebar.success('Select a demo above to get started.')

st.image('./source/photo-stickers.jpg', caption='Photo-Stickers From My GitHub')

st.markdown(
f'''
#### About Me
Hi, I'm Ping Chun Wu, a passionate developer with a focus on `Data Science`, `Machine Learning`, and `Software Development`. 
I enjoy solving complex problems and continuously learning to improve my skills.


#### Expertise
###### About Python Skills
 - Master : Strings, List, Tuple, Dict, Set, For Loop, Array, DataFrame, `Class`, `Inheritance`, ...etc.
 - Commonly Used : PyTorch, TensorFlow, Keras, Scikit-Learn, pickle, datasets, OpenCV, PIL, requests, NumPy, Pandas, BeautifulSoup, Selenium, Plotly, ArgumentParser, LineBotSDK, WebSocket, ThreadPoolExecutor, os, datetime, decimal, copy, json, flask, rich, tqdm, matplotlib, schedule, time, ...etc.

###### About Programming
 - Frontend : HTML / CSS / Markdown
 - Backend : `Python` / PHP / C / C++
 - DataBase : `SQL Server`
 - Version Control : `GitHub`
 - Deploy : `Docker`
 - Transport Protocol : MQTT / WebSocket
 - Operating System : Windows / Linux
 - Other : WampServer / NGROK / Git-Gist / Git Action / GistHub.io

###### About Production Software
 - Job Tool : `ChatGPT` / `Github Copilot` / `Youtrack` / Notion
 - Programming Environment : `PyCharm` / Jupyter / Spyder / VScode / VS
 - Microsoft Office : Excel / Word / PowerPoint
 - Adobe Software : Photoshop / Premiere / After Effects / Acrobat
'''
)