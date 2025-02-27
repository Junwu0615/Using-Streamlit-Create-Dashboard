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

# st.markdown(f"""
# | <div style='width: 100px'> Concept </div> | <div style='width: 80px'> Directions </div> | <div style='width: 200px'> Technologies </div> | <div style='width: 300px'> Coverage </div> |
# |:--|:--|:--|:--|
# | PLAN | 需求與變更管理 | GitHub Projects / Notion | :blue-background[Agile Development] / :blue-background[Defined CI/CD Pipeline] / :blue-background[Version Management] | # Agile 管理開發週期 / 明確定義 CI/CD Pipeline / 版本管理(GitOps)
# | CODE | 版本控制 | GitHub | :blue-background[Git Flow] / PR / Code Quality Management | # Git Flow / PR / 代碼質量管理 ( SonarQube )
# | BUILD | 建置應用程式 | Python / Docker | :blue-background[CICD Pipeline] / :blue-background[Docker Build] / Docker Hub |
# | TEST |自動化測試 | Python | :blue-background[Unit Testing] / End-to-End Testing / Service Testing / Security Testing / Load Testing | # 單元測試 / 端對端測試 / 服務測試 / 安全測試 / 負載測試
# | RELEASE | 版本管理與交付 | GitHub Releases / Docker | :blue-background[Git Tag Mapping Docker Image Tags] / :blue-background[Automated Release Process] |
# | DEPLOY | 部署 | Docker / Kubernetes | :blue-background[Dev　→　Staging　→　Prod] | # 開發環境(Dev)　→　測試環境(Staging)　→　正式環境(Prod) 分層部署
# | OPERATE | 運維與監控 | Kubernetes / Helm | - |
# | MONITOR | 監控與告警 | Prometheus / Grafana / Telegram | :blue-background[Monitor] / :blue-background[Log Management] / :blue-background[Alertmanager] | # 監控 K8S 資源、API、流量 # Loki：集中日誌管理 # Alertmanager：告警機制 (整合 Slack / Telegram)
#
# """, unsafe_allow_html=True)

st.markdown(f"""
<table border="1">
  <tr>
    <th align="center" rowspan="2">Group</th>
    <th align="center" rowspan="2">Concept</th>
  </tr>
  <tr>
    <th align="center">Project Name</th>
    <th align="center">Task</th>
    <th align="center">Technologies</th>
  </tr>
  <tr>
    <td align="center" rowspan="10">DevOps Team</td>
    <td align="center" rowspan="2">CODE<br>CI/CD Pipeline</td>
    <td align="left">-</td>
    <td align="left">CI/CD 自動化</td>
    <td align="left">GitHub Actions / GitLab CI / Jenkins</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">CD 部署工具</td>
    <td align="left">ArgoCD / FluxCD</td>
  </tr>
  <tr>
    <td align="center" rowspan="2">RELEASE<br>基礎架構管理</td>
    <td align="left">-</td>
    <td align="left">Infrastructure as Code</td>
    <td align="left">Terraform / Pulumi / AWS CDK</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">雲端資源管理</td>
    <td align="left">AWS, GCP, Azure</td>
  </tr>
  <tr>
    <td align="center" rowspan="3">OPERATE & MONITOR<br>監控與告警</td>
    <td align="left">-</td>
    <td align="left">監控系統</td>
    <td align="left">Prometheus / Grafana</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Log 監控</td>
    <td align="left">ELK Stack / Loki</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">告警系統</td>
    <td align="left">AlertManager / PagerDuty</td>
  </tr>
  <tr>
    <td align="center" rowspan="3">BUILD & DEPLOY<br>配置管理</td>
    <td align="left">-</td>
    <td align="left">Docker</td>
    <td align="left">Docker / Docker Compose</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Kubernetes 部署</td>
    <td align="left">K8s, Helm, Istio</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Secrets 管理</td>
    <td align="left">HashiCorp Vault / AWS Secrets Manager</td>
  </tr>
    <tr>
    <td align="center" rowspan="5">Dev Team</td>
    <td align="center" rowspan="5">PLAN & CODE<br>應用程式開發</td>
    <td align="left">-</td>
    <td align="left">Web API</td>
    <td align="left">FastAPI / Express.js / Flask</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Front-end Web App</td>
    <td align="left">React / Vue / Angular</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">AI / ML Service</td>
    <td align="left">TensorFlow / PyTorch</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Mobile App</td>
    <td align="left">Flutter / React Native</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Serverless Function</td>
    <td align="left">AWS Lambda / Cloud Functions</td>
  </tr>
  <tr>
    <td align="center" rowspan="5">QA Team</td>
    <td align="center" rowspan="5">TEST<br>測試自動化</td>
    <td align="left">-</td>
    <td align="left">Unit Testing</td>
    <td align="left">PyTest / JUnit / Jest</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">End-to-End Testing</td>
    <td align="left">Cypress / Selenium</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Service Testing</td>
    <td align="left">-</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Security Testing</td>
    <td align="left">OWASP ZAP / SonarQube</td>
  </tr>
  <tr>
    <td align="left">-</td>
    <td align="left">Load Testing</td>
    <td align="left">K6 / JMeter</td>
  </tr>
</table>
""", unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)