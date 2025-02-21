# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-02-21
"""
import streamlit as st
from depend.visit_count_logic import visit_count
from settings import LIGHT, DARK, DEFAULT

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='DevOps Concept Implementation',
    page_icon='⚙️',
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
<img alt="Visit_Count" src="https://img.shields.io/badge/Visit_Count-{visit_count('C6')}-blue?logo=ferrari&style=flat-square">
""", unsafe_allow_html=True)

st.markdown('## :rainbow[*DevOps Concept Implementation*]', unsafe_allow_html=True, help='Beta Testing')
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<a href="https://line.me/R/ti/p/@059dtndx" target="_blank">
    <img height=400 weight=400 src="https://raw.githubusercontent.com/Junwu0615/Using-Streamlit-Create-Dashboard/main/source/DevOps.png" >
</a>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
| <div style='width: 100px'> Concept </div> | <div style='width: 80px'> Directions </div> | <div style='width: 200px'> Technologies </div> | <div style='width: 300px'> Coverage </div> |
|:--|:--|:--|:--|
| PLAN | 需求與變更管理 | GitHub Projects / Notion | :blue-background[Agile Development] / :blue-background[Defined CI/CD Pipeline] / :blue-background[Version Management] | # Agile 管理開發週期 / 明確定義 CI/CD Pipeline / 版本管理(GitOps)
| CODE | 版本控制 | GitHub | :blue-background[Git Flow] / PR / Code Quality Management | # Git Flow / PR / 代碼質量管理 ( SonarQube )
| BUILD | 建置應用程式 | Python / Docker | :blue-background[CICD Pipeline] / :blue-background[Docker Build] / Docker Hub |
| TEST |自動化測試 | Python | :blue-background[Unit Testing] / End-to-End Testing / Service Testing / Security Testing / Load Testing | # 單元測試 / 端對端測試 / 服務測試 / 安全測試 / 負載測試
| RELEASE | 版本管理與交付 | GitHub Releases / Docker | :blue-background[Git Tag Mapping Docker Image Tags] / :blue-background[Automated Release Process] |
| DEPLOY | 部署 | Docker / Kubernetes | :blue-background[Dev　→　Staging　→　Prod] | # 開發環境(Dev)　→　測試環境(Staging)　→　正式環境(Prod) 分層部署
| OPERATE | 運維與監控 | Kubernetes / Helm | - |
| MONITOR | 監控與告警 | Prometheus / Grafana / Telegram | :blue-background[Monitor] / :blue-background[Log Management] / :blue-background[Alertmanager] | # 監控 K8S 資源、API、流量 # Loki：集中日誌管理 # Alertmanager：告警機制 (整合 Slack / Telegram)

""", unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)