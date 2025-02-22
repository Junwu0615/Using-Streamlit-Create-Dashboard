# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-01-06
"""
import json
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from depend.visit_count_logic import visit_count
from settings import LIGHT, DARK, DEFAULT

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='Side Project',
    page_icon='📋',
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
<img alt="Visit_Count" src="https://img.shields.io/badge/Visit_Count-{visit_count('C3')}-blue?logo=ferrari&style=flat-square">
""", unsafe_allow_html=True)

st.markdown('## :rainbow[*OPEN SOURCE PROJECT*]', unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        'LLM',
        'Machine Learning',
        'Backend',
        'Data Visualization',
        'Web Crawler',
    ])

with tab1:
    # LLM
    st.markdown("""
    | <div style='width: 230px'> Title </div> | <div style='width: 80px'> Clone </div> | <div style='width: 300px'> Technologies </div> |
    |--|:--:|--|
    | [PC-Bot-With-GenAI](https://github.com/Junwu0615/PC-Bot-With-GenAI) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/8c304a23bb8dad13ba9658dbaa3f806c/raw/PC-Bot-With-GenAI_clone.json&logo=github"> | ![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2.svg?logo=googlegemini&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E.svg?logo=amazonwebservices&logoColor=white) ![Azure](https://img.shields.io/badge/Azure-005571.svg?logo=data:image/png;base64,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&logoColor=white) ![GCP](https://img.shields.io/badge/GCP-0067A0.svg?logo=googlecloud&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=docker&logoColor=white)<br>![SQL_Server](https://img.shields.io/badge/SQL_Server-646565.svg?logo=data:image/jpeg;base64,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) ![Line](https://img.shields.io/badge/Line-00c300.svg?logo=line&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000.svg?logo=flask&logoColor=white) ![NGROK](https://img.shields.io/badge/NGROK-1F1E37.svg?logo=ngrok&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    """, unsafe_allow_html=True)

with tab2:
    # Machine Learning
    st.markdown("""
    | <div style='width: 230px'> Title </div> | <div style='width: 80px'> Clone </div> | <div style='width: 300px'> Technologies </div> |
    |--|:--:|--|
    | [LCII-Rec-Model](https://github.com/Junwu0615/LCII-Rec-Model) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/7f654406c51d568d31d565347f22d609/raw/LCII-Rec-Model_clone.json&logo=github"> | ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?logo=tensorflow&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [NVDA-Price-Stock-Prediction](https://github.com/Junwu0615/NVDA-Price-Stock-Prediction) |  <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/05f5b34eedbee0ef7d196fdb42ee61f6/raw/NVDA-Price-Stock-Prediction_clone.json&logo=github"> | ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000.svg?logo=keras&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    """, unsafe_allow_html=True)

with tab3:
    # Backend
    st.markdown("""
    | <div style='width: 230px'> Title </div> | <div style='width: 80px'> Clone </div> | <div style='width: 300px'> Technologies </div> |
    |--|:--:|--|
    | [CAED feat.DL](https://github.com/dl-jack-123/CAED) | <img alt='GitHub Views' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/dl-jack-123/7b40f4b7a8ef0f41258dd5343a77e1a9/raw/CAED_clone.json&logo=github](https://github.com/Junwu0615/How-To-Use-Clone-Shields'> | ![Apache_Airflow](https://img.shields.io/badge/Apache_Airflow-000000.svg?logo=apacheairflow&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1.svg?logo=PostgreSQL&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Airflow-Template](https://github.com/Junwu0615/Airflow-Template) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/c7cc2b44b987253f9efcf042e839837e/raw/Airflow-Template_clone.json&logo=github"> | ![Apache_Airflow](https://img.shields.io/badge/Apache_Airflow-000000.svg?logo=apacheairflow&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Database-Template](https://github.com/Junwu0615/Database-Template) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/65eaa98eafcee3f625a269fa70451f8a/raw/Database-Template_clone.json&logo=github"> | ![SQL_Server](https://img.shields.io/badge/SQL_Server-646565.svg?logo=data:image/jpeg;base64,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) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Forex-Get-Quotes](https://github.com/Junwu0615/Forex-Get-Quotes) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/4bb80a5b6974941fbee54b711ec077bc/raw/Forex-Get-Quotes_clone.json&logo=github"> | ![SQL_Server](https://img.shields.io/badge/SQL_Server-646565.svg?logo=data:image/jpeg;base64,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) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) ![Telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?logo=telegram&logoColor=white) ![Line](https://img.shields.io/badge/Line-00c300.svg?logo=line&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [RESTful-API-FastAPI](https://github.com/Junwu0615/RESTful-API-FastAPI) | <img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/732741678dbe23fa2369b6a0c13846fa/raw/RESTful-API-FastAPI_clone.json&logo=github'> | ![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?logo=fastapi&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [NGROK-Dockerization](https://github.com/Junwu0615/NGROK-Dockerization) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/2792e35583530c4e1c58662bbb5a49da/raw/NGROK-Dockerization_clone.json&logo=github"> | ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) |
    | [Cloudflare-Dockerization](https://github.com/Junwu0615/Cloudflare-Dockerization) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/65175b78909744f87ef7330aba1945b4/raw/Cloudflare-Dockerization_clone.json&logo=github"> | ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=Docker&logoColor=white) |
    | [The-First-PHP-Login-System](https://github.com/Junwu0615/The-First-PHP-Login-System) |  <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/ab14c4824b25cc2eb94c56e63b133e32/raw/The-First-PHP-Login-System_clone.json&logo=github"> | ![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?logo=MySQL&logoColor=white) ![Wampserver](https://img.shields.io/badge/Wampserver-C6007E.svg?logo=wasmcloud&logoColor=white) ![PHP](https://img.shields.io/badge/PHP-777BB4.svg?logo=PHP&logoColor=white) |
    """, unsafe_allow_html=True)

with tab4:
    # Data Visualization
    st.markdown("""
    | <div style='width: 230px'> Title </div> | <div style='width: 80px'> Clone </div> | <div style='width: 300px'> Technologies </div> |
    |--|:--:|--|
    | [Using-Streamlit-Create-Dashboard](https://github.com/Junwu0615/Using-Streamlit-Create-Dashboard) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/bba308b4514074dc7b93d762906f329b/raw/Using-Streamlit-Create-Dashboard_clone.json&logo=github"> | ![Streamlit](https://img.shields.io/badge/Streamlit-167C80.svg?logo=streamlit) ![Streamlit_Cloud](https://img.shields.io/badge/Streamlit_Cloud-41454A.svg?logo=icloud) ![Google_Sheet](https://img.shields.io/badge/Google_Sheet-3F4F95.svg?logo=googlesheets) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75.svg?logo=plotly) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    """, unsafe_allow_html=True)

with tab5:
    # Web Crawler
    st.markdown("""
    | <div style='width: 230px'> Title </div> | <div style='width: 80px'> Clone </div> | <div style='width: 300px'> Technologies </div> |
    |--|:--:|--|
    | [Crawler-Keywords-And-Use-LineBot](https://github.com/Junwu0615/Crawler-Keywords-And-Use-LineBot) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/dc62dfdf2b0e2710dd9a47cebee51ffa/raw/Crawler-Keywords-And-Use-LineBot_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![Line](https://img.shields.io/badge/Line-00c300.svg?logo=line&logoColor=white) ![NGROK](https://img.shields.io/badge/NGROK-1F1E37.svg?logo=ngrok&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000.svg?logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [LeetCode-Record-Sharing-Method](https://github.com/Junwu0615/LeetCode-Record-Sharing-Method) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.github.com/Junwu0615/df4349f01a564de4cf309a290098ba58/raw/LeetCode-Record-Sharing-Method_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![LeetCode](https://img.shields.io/badge/LeetCode-FFA116.svg?logo=leetcode&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white)|
    | [Downloads-YouTube-To-MP3&MP4](https://github.com/Junwu0615/Downloads-YouTube-To-MP3-4)| <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/acb7aeb93f554e94a7a6db8e909bc0c6/raw/Downloads-YouTube-To-MP3-4_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![YouTube](https://img.shields.io/badge/YouTube-C5242C.svg?logo=YouTube&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Web-Crawler-News](https://github.com/Junwu0615/Web-Crawler-News) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/d1d16a79eeb95ac0c3e99a279c3b7365/raw/Web-Crawler-News_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![CSV](https://img.shields.io/badge/CSV-44825D.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACOEfKtAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEjklEQVR4nO2YCU8TQRTH++G8o1Gj8SKAIJGopGgUvFC0RZBLJOUoUMrZWrlLLbVba1RUItGAeF8w3+SZt7jbmS3FkpjszPomeQnMvJltf/3PvP+sy0WNGjVq1PJuRYFqkDEKA1ULSvyMdoMqUh2i8WE1lpYijM9TEryyDrG36qVL5iYrwMXVlQxEmZUoK0BsSkCUGaASEGUHKD1EFQBKDVEVgNJCVAmglBBVAygdRBUBSgVRVYDSQFQZoBQQVQdoO0QnALQVolMA2gbRSQBtgSgrwKJ/FAQwQADBTiX/dwrUCGDadnikQEYAgRTI7IdAW5gRQLBbSVREGAEEu9VENoYRQMgFIfotDr7nQWhMdsL9p30QeT+VlZNYS0HwTRhaUn5oSnVDz+thiP9K6mOPfjyG3oVRMyIr05b154Tx8U9RZxjpma9xOB+6Ddu9RbDNU2jGwZZyIa9zfkDv43MwCjoq9fHZbwnY7smsUTF8Q5iP0Pl53fOD6gOc+BiFw21ns6BgnBm4LsDj4fBxjgN1pL3C7D/ucwvPujpx1xzDtfCHUxrg49UUFHZdEGAcuX8OqsfqdUU2aV1mHq+83XdK9PHL4w1w0n8JPLE2c03sN/J21hXrc42x8uA17jkVeX9OaQG2PhG3VGXoln7GWfOG3kaEPDy/rD+E8Xez1iXkRlYy5yiv9Athj/oACzoqzS+0v7kc4j/Xi4E1sLDwUHLlYYSWJoTczhcDej8Wmm3eTD+eh0oDnPkaF840PJ9y5WLV5aFglc659loa9jSUmrm3/2zv0NK4sMaDDSq8UgD9r4aFL+R73r/pWSlUX28h1Ew3Q4LbunyU9VWbue6RWr2v/VnA7NvbeAqS7InaAO+lewWAQ28fbpqPAKxV+LivMsvrYdycacmyOLXRVrMPi0m+8KQF2JDwCTDCy5N/nVMXb8/yirhdw0sTOdWN46g2vjp7HrWpD7Ax2SmAGH63uQKN6FsYgQMWM42WJLmW2ZJWQz31OQbF/ovm//1vQuoDbOfOJL1azq9Xy3wCr2QlPVXCfP+rISGHN9TBxbBe5XVv6C2GuZ+a+gBHLXajZqppS18Kq/iu+pPm/Fuz94Rx9HnGGB4XhiLRuG/lOdICTKylYF9jmXDvnfu1NWUc5VSGVZkfa9a6zbHT/VfNv6+MNzgDoMbScClSJ6jQPVq7oTVBG4PnmlXBuB2Nufj2hh/HwsJf/Uy79KzfOQAnP8eEbWgoEV8OoJerT/j0vJF3Y7CjrhhKe6r0anp2sEaAgr5u9ntiU0NtBD7TMQC1P9c0qzUxAmFhTpvFMwrhRRMe3HDtssBlIfdQ65ktw5MeoIZXtcUwnPC5s+CU9q6vhS9O+e1qxDGfO+vFAh83oxlDzd9KHAdQM86t5UndzqDi8E1z7PucYF3wToxnHSouH+M9/SUmvIEe+zDjbICapEEAGQEEUiCzfyvSFmYEEOxWExURRgDBbkWRjWEEEFQKMtKMAAIpkNm/FWkLMwIIdquJiggjgGC3osjGMAIIKgUZaaYYQKeGiwBWyw2QGjVq1FzOab8B0guUXk04wx0AAAAASUVORK5CYII=) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Web-Crawler-FamilyMart-Shop](https://github.com/Junwu0615/Web-Crawler-FamilyMart-Shop) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/6d7399737815a21d2dce1ad86f2937c2/raw/Web-Crawler-FamilyMart-Shop_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![CSV](https://img.shields.io/badge/CSV-44825D.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACOEfKtAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEjklEQVR4nO2YCU8TQRTH++G8o1Gj8SKAIJGopGgUvFC0RZBLJOUoUMrZWrlLLbVba1RUItGAeF8w3+SZt7jbmS3FkpjszPomeQnMvJltf/3PvP+sy0WNGjVq1PJuRYFqkDEKA1ULSvyMdoMqUh2i8WE1lpYijM9TEryyDrG36qVL5iYrwMXVlQxEmZUoK0BsSkCUGaASEGUHKD1EFQBKDVEVgNJCVAmglBBVAygdRBUBSgVRVYDSQFQZoBQQVQdoO0QnALQVolMA2gbRSQBtgSgrwKJ/FAQwQADBTiX/dwrUCGDadnikQEYAgRTI7IdAW5gRQLBbSVREGAEEu9VENoYRQMgFIfotDr7nQWhMdsL9p30QeT+VlZNYS0HwTRhaUn5oSnVDz+thiP9K6mOPfjyG3oVRMyIr05b154Tx8U9RZxjpma9xOB+6Ddu9RbDNU2jGwZZyIa9zfkDv43MwCjoq9fHZbwnY7smsUTF8Q5iP0Pl53fOD6gOc+BiFw21ns6BgnBm4LsDj4fBxjgN1pL3C7D/ucwvPujpx1xzDtfCHUxrg49UUFHZdEGAcuX8OqsfqdUU2aV1mHq+83XdK9PHL4w1w0n8JPLE2c03sN/J21hXrc42x8uA17jkVeX9OaQG2PhG3VGXoln7GWfOG3kaEPDy/rD+E8Xez1iXkRlYy5yiv9Athj/oACzoqzS+0v7kc4j/Xi4E1sLDwUHLlYYSWJoTczhcDej8Wmm3eTD+eh0oDnPkaF840PJ9y5WLV5aFglc659loa9jSUmrm3/2zv0NK4sMaDDSq8UgD9r4aFL+R73r/pWSlUX28h1Ew3Q4LbunyU9VWbue6RWr2v/VnA7NvbeAqS7InaAO+lewWAQ28fbpqPAKxV+LivMsvrYdycacmyOLXRVrMPi0m+8KQF2JDwCTDCy5N/nVMXb8/yirhdw0sTOdWN46g2vjp7HrWpD7Ax2SmAGH63uQKN6FsYgQMWM42WJLmW2ZJWQz31OQbF/ovm//1vQuoDbOfOJL1azq9Xy3wCr2QlPVXCfP+rISGHN9TBxbBe5XVv6C2GuZ+a+gBHLXajZqppS18Kq/iu+pPm/Fuz94Rx9HnGGB4XhiLRuG/lOdICTKylYF9jmXDvnfu1NWUc5VSGVZkfa9a6zbHT/VfNv6+MNzgDoMbScClSJ6jQPVq7oTVBG4PnmlXBuB2Nufj2hh/HwsJf/Uy79KzfOQAnP8eEbWgoEV8OoJerT/j0vJF3Y7CjrhhKe6r0anp2sEaAgr5u9ntiU0NtBD7TMQC1P9c0qzUxAmFhTpvFMwrhRRMe3HDtssBlIfdQ65ktw5MeoIZXtcUwnPC5s+CU9q6vhS9O+e1qxDGfO+vFAh83oxlDzd9KHAdQM86t5UndzqDi8E1z7PucYF3wToxnHSouH+M9/SUmvIEe+zDjbICapEEAGQEEUiCzfyvSFmYEEOxWExURRgDBbkWRjWEEEFQKMtKMAAIpkNm/FWkLMwIIdquJiggjgGC3osjGMAIIKgUZaaYYQKeGiwBWyw2QGjVq1FzOab8B0guUXk04wx0AAAAASUVORK5CYII=) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Web-Crawler-Download-Img](https://github.com/Junwu0615/Web-Crawler-Download-Img) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/706da0097d75deeae8342f2203db8b19/raw/Web-Crawler-Download-Img_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white)|
    | [Parsing-Media-From-PornHub](https://github.com/Junwu0615/Parsing-Media-From-PornHub) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.github.com/Junwu0615/c5c70b3f72648a0bc59f2a7a530b3e32/raw/Parsing-Media-From-PornHub_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![Pornhub](https://img.shields.io/badge/Porn-hub-FD9900.svg?logo=data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEOUlEQVR4nO2Wa2xURRTHp9uGdmmtULYspLc75z97eVikWg0JGNNGiwo0pqFBFPmABMNLLGgEhFXA+JZES0gpa0ggoB/0A1KtJkRifGsUNSR+wA/GBBONWnwvSqSOmbszt7e3C9ptd7uYe5KT7P7nzNzzmzln7mUssMACC6wgjYiOex3AWwC6ARzgnM9nhW4A5L/4WlbIBp0oEXUCmMs5n0dEKwF8o/WfLcsKs4sAYL1XJ6JlZkwIMdPotm2XCiFuB9BFRM8R0YPxeLzWN/cmItoshLieiFqJ6JD6zxgLAbhXj01UcQCe1Zt3C2OsaCQBVvkBAEQBfJqhzFIAbvas2aXX/BhAn/59XI+l9JwjGdZJZA0AYL/aBSHEGgBPAjij9W+bmppKdOxLWusFsEI1OYA3tPa7OQkDoL2biDYKIZb4AHqFEC1EdAURfaS1r4YDMMiJ6KzZWdu2LbObqoTMfNu2KwGc1vHbfCfwG+e8zPc8B4CIHvdoa7X253AAThLR6wAOE9E+ItpORNzE6Xp1Yi3LqvGuQUTH9NgLPoAvMjwvpWPXeeYvNmuPWA/4jYgaTWwsFhO+sXf12EEvAIAPLwCw1DO/NecAlmVV6ZJSsZuMzjknAH8onXO+2gdw9HwAwlOGeQHQsUkdf05dfwB2ENEprX0ZjUbLfQCvFRSAZVlh9YkB4G9fs5+Ix+O2Z828AsxV7n8ZXchUD6gXHRG1CyGaGWPF3nHO+XT9Vm/wz+WcX6fHJhnNtu1qk8eQAQIbbetLslf7kkwWiPdkAyALyVkAkPwfnED3hgr5/JpL5Nc7S4ad0Htbw85an+0ozR9AY0Ot81I5tnHssAHaW6qdtXYuHR8AZHUCJx8dI/fdWSlfvKtC/rQr5Mac7gjJd7aE5QcPlA0qGaX/sjs06AROPVUiD6yslEfWV8jvnynOfQnd0RyVdrz/m2d2fUz+oB+sElXarMtjA+ZOn0KOfuKh0gEAi66dLGdO4+5aV9XF5PuJstwCqIRVQx+9b6xsqEs/XJ1GNgBxAdm1/FIn6WXNkxxtTn1Mnu0qyh3AnuXjXG3dgomO9sitVVkBrLgh6sZ893SxA6T0zx8ekzuAVzaUu1qiLeJoibYJAwCuntEP8Nde5pacH+CJJWlw4wpc6ep083KNbls0ISOA2nET8+OukFvjfoBEW2TAM0w/+PsgbwCfbC91k+3tSDe2SuZ8AHPqY7K3I30zvb0lDa/KSJXTqAD8ujsk66am6/3GWTVyU2vEaXSj+QHqppK8pr5WrpoXlTOmpWPuXlCdm1uoZXaNvPIyLt/cHHa1x26rcjTTxMp77il3a1ndWIfbK+TixslOnGnO+xdGnP+HVlc6yatdnxInubUtIlOdRbkBGIqf25uu/f8an+oskmcyJD5qACPtLABIXnwn0DPaSff1+8tDBggssMACY/mwfwCikBK6t0Uc4QAAAABJRU5ErkJggg==) ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808.svg?logo=ffmpeg&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    | [Parsing-Media-From-JVID](https://github.com/Junwu0615/Parsing-Media-From-JVID) | <img alt="Clone" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.github.com/Junwu0615/95457ff8b4eae84b4e855461cdc34ab4/raw/Parsing-Media-From-JVID_clone.json&logo=github"> | ![Crawler](https://img.shields.io/badge/Crawler-006241.svg?logo=openbugbounty&logoColor=white) ![JVID](https://img.shields.io/badge/JVID-DA3B8A.svg?logo=youtube&logoColor=white) ![FFmpeg](https://img.shields.io/badge/FFmpeg-007808.svg?logo=ffmpeg&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white) |
    """, unsafe_allow_html=True)


st.markdown('---', unsafe_allow_html=True)
st.markdown('## :rainbow[*PROPRIETARY PROJECT*]', unsafe_allow_html=True)

st.markdown('##### A . LCII-Rec-Model Performance', unsafe_allow_html=True)
st.markdown("""
###### [:blue-background[Master's thesis]](https://drive.google.com/file/d/1HhYjno6EakDS5pmoGHuOYHQ-gmq1K3o_/view)  [:blue-background[Journal Link]](https://drive.google.com/file/d/1Qx60S7cAOJsBpTvEVzufoSP0u5ImSI8V/view?usp=sharing)
""", unsafe_allow_html=True, help='Note : The translator has a translation error')

@st.cache_data
def load_data_1():
    loader = json.loads(''.join([i for i in open('./source/lcii_performance.json')]))[0]
    return loader
df1 = pd.DataFrame(load_data_1())

edited_df1 = st.data_editor(
    pd.DataFrame({'Dataset': ['Amazon']}),
    column_config={
        'Dataset': st.column_config.SelectboxColumn(
            'Choose Dataset',
            help='選擇欲呈現 [資料集]',
            width='medium',
            options=[
                'Amazon',
                'MovieLens 1M',
                'Steam',
            ],
            required=True,
        )
    },
    hide_index=True,
)
s = df1[df1['Dataset'] == edited_df1['Dataset'].values[0]][df1.columns[1:]].style \
    .highlight_max(subset=df1.columns[2:], color=st.session_state['df_color'], axis=0) \
    .set_properties(**{'text-align': 'center'}) \
    .format(precision=3, decimal='.')
st.dataframe(s, height=len(df1.index)*13, hide_index=True, use_container_width=True)



st.markdown('<br>', unsafe_allow_html=True)
st.markdown('##### B . Prediction Trading Volume Performance', unsafe_allow_html=True)
st.markdown("""
- ###### 台股標的有 1800 多個 Symbol ，擁有充分數據量的只有 804 個 Symbol。基於 `K-means` 用來劃分同性質標的，進一步擴展數據量。用 `GRU` 預測結果如下表所示。
    - ###### Unit (%)
    - ###### Min / Max : 檢視極端值性能狀態 :blue-background[( 預期 : 各標的表現不差距過大 )]
    - ###### IQR : 檢視各級距性能分布狀態 :blue-background[( 預期 : 各標的表現不差距過大 )]
    - ###### Rate : 檢視小於指定數值範圍，其占整體比重幾何 ex: 性能不超過 10 % 佔比幾何 :blue-background[( 預期 : 越小越好 )]
""", unsafe_allow_html=True)

@st.cache_data
def load_data_2():
    loader = json.loads(''.join([i for i in open('./source/pv_performance.json')]))[0]
    return loader
df2 = pd.DataFrame(load_data_2())

edited_df2 = st.data_editor(
    pd.DataFrame({'Model': ['I.　Clusters Model [108]']}),
    column_config={
        'Model': st.column_config.SelectboxColumn(
            'Choose Clusters Model',
            help='選擇欲呈現 [基於集群分類之模型]',
            width='medium',
            options=[
                'I.　Clusters Model [108]',
                'II.　Clusters Model [318]',
                'III.　Clusters Model [3]',
                'IV.　Clusters Model [18]',
                'VI.　Clusters Model [357]',
            ],
            required=True,
        )
    },
    hide_index=True,
)
cm = sns.light_palette('green', as_cmap=True)
s = df2[(df2['Model'] == edited_df2['Model'].values[0])][df2.columns[1:]].style \
    .set_properties(**{'text-align': 'center'}) \
    .format(precision=3, decimal='.') \
    .background_gradient(cmap=cm)
st.dataframe(s, height=len(df2.index)*8, hide_index=True, use_container_width=True)



st.markdown('''<style>
    .stTabs [data-baseweb='tab-list']
    button [data-testid='stMarkdownContainer']
    p { font-size:1.2rem; }
</style>''', unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)