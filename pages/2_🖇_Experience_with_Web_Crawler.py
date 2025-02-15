# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2025-02-12
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
    page_title='Experience with Web Crawler',
    page_icon='🖇️',
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
<img alt="Visit_Count" src="https://img.shields.io/badge/Visit_Count-{visit_count('C4')}-blue&logo=github">
""", unsafe_allow_html=True)

st.markdown('## :rainbow[*Experience with Web Crawler*]')
col1, col2 = st.columns([1, 0.5]) # 寬度比例
with col1:
    st.markdown("""
    #### Before initiating any :blue-background[web crawler], I ensure the following steps :
    - Define the `data table specifications` of database.
    - Determine the `most efficient` method for extracting resources from the target website.
      - API
      - HTML
      - Script
      - CSV / Excel
    - Implement `ETL` logic.
      - `Extract`：download data from the data source
      - `Transform`：clean and format the data
      - `Load`：store the data in the database
    - Automate `deployment`.
    #### Experienced with :rainbow[60] types of web crawlers, as shown below.
    <br>
    """, unsafe_allow_html=True)
with col2:
    pass

st.markdown("""###### :blue-background[⭐ Other Platform Resources]""", help='其他平台資源')
marquee_1 = """
<div style="width: 100%; overflow: hidden; white-space: nowrap; box-sizing: border-box; background-color: white; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
    <div style="display: inline-block; animation: marquee 22s linear infinite;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png" alt="Google" height="55px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/2560px-YouTube_Logo_2017.svg.png" alt="youtube" height="30px" style="margin: 0 20px;">
        <img src="https://pngimg.com/uploads/github/github_PNG23.png" alt="GitHub" height="60px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/LeetCode_Logo_black_with_text.svg/2560px-LeetCode_Logo_black_with_text.svg.png" alt="LeetCode" height="40px" style="margin: 0 20px;">
        <img src="https://i.imgur.com/XwoKyiS.jpeg" alt="PTT" height="90px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/104_logo.png/1200px-104_logo.png" alt="104" height="30px" style="margin: 0 20px;">
        <img src="https://lh4.googleusercontent.com/-c0MO3an6LW0bk_-nx3FfZwytUPRPFocKsrh6P18NPGSUz5NgnVD0-Rt8Tc0t3m-11aXZZRH6ofdCryQuW_achRtARicWKRUXwg5w4s85OqWpniiG2mpV8xlifkozayFUVFlM6EW" alt="cake" height="100px" style="margin: 0 20px;">
        <img src="https://static.wixstatic.com/media/cc8b39_74e1637c716840fcb4dc1d0f07868a94~mv2.jpg/v1/fill/w_876,h_344,al_c/cc8b39_74e1637c716840fcb4dc1d0f07868a94~mv2.jpg" alt="yourator" height="100px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtZ7ZArYB9mBrBw4WJA7Oqf2d7kOqA41DYzw&s" alt="goodjob" height="80px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTISSeEHJJ_JoA50xJ8M7yXyUogbXw1GX4ctw&s" alt="pornhub" height="50px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-h1Z5--PFgKXN_kIDwmMLDPb0UPYkA5wqkQ&s" alt="全家" height="30px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png" alt="Google" height="55px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/2560px-YouTube_Logo_2017.svg.png" alt="youtube" height="30px" style="margin: 0 20px;">
        <img src="https://pngimg.com/uploads/github/github_PNG23.png" alt="GitHub" height="60px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/LeetCode_Logo_black_with_text.svg/2560px-LeetCode_Logo_black_with_text.svg.png" alt="LeetCode" height="40px" style="margin: 0 20px;">
        <img src="https://i.imgur.com/XwoKyiS.jpeg" alt="PTT" height="90px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/104_logo.png/1200px-104_logo.png" alt="104" height="30px" style="margin: 0 20px;">
        <img src="https://lh4.googleusercontent.com/-c0MO3an6LW0bk_-nx3FfZwytUPRPFocKsrh6P18NPGSUz5NgnVD0-Rt8Tc0t3m-11aXZZRH6ofdCryQuW_achRtARicWKRUXwg5w4s85OqWpniiG2mpV8xlifkozayFUVFlM6EW" alt="cake" height="100px" style="margin: 0 20px;">
        <img src="https://static.wixstatic.com/media/cc8b39_74e1637c716840fcb4dc1d0f07868a94~mv2.jpg/v1/fill/w_876,h_344,al_c/cc8b39_74e1637c716840fcb4dc1d0f07868a94~mv2.jpg" alt="yourator" height="100px" style="margin: 0 20px;">
    </div>
</div>
"""
st.markdown(marquee_1, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""###### :blue-background[⭐ [Fintech] Foreign Platform Resources]""", help='[金融科技] 海外平台資源')
marquee_2 = """
<div style="width: 100%; overflow: hidden; white-space: nowrap; box-sizing: border-box; background-color: white; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
    <div style="display: inline-block; animation: marquee 27s linear infinite;">
        <img src="https://i.pinimg.com/736x/94/85/e9/9485e913620577eff748a7b28f263a8b.jpg" alt="TradingView" height="50px" style="margin: 0 20px;">
        <img src="https://i.pinimg.com/736x/25/35/1d/25351d37543b591621eb8e522d81674d.jpg" alt="Investing.com" height="40px" style="margin: 0 20px;">
        <img src="https://d3g3pd9iiem0rf.cloudfront.net/public-eu-central-1/providers/a43209e9-c753-48df-a85d-9e3e55149ec6/brand-logo/Logo_light_2x_d95450c472d9f75d.png" alt="FMP" height="70px" style="margin: 0 20px;">
        <img src="https://www.shutterstock.com/image-illustration/isin-international-security-identification-number-260nw-2197952243.jpg" alt="ISIN" height="80px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsZk1WMFJImgtpushlYrpbH3SddAdgifJFnw&s" alt="幣安" height="40px" style="margin: 0 20px;">
        <img src="https://higherlogicdownload.s3.amazonaws.com/AAII/657bf0c9-a6b1-489f-aca1-1fc86e9beae3/UploadedImages/AAII-and-type-next-to-it_blue.png" alt="AAII" height="45px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Yahoo%21_Finance_logo_2021.png" alt="Yahoo_Finance" height="50px" style="margin: 0 20px;">
        <img src="https://companieslogo.com/img/orig/S68.SI_BIG-dfecdb4f.png?t=1720244493" alt="SGX" height="40px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/HKEX_logo_2016.svg/2560px-HKEX_logo_2016.svg.png" alt="HKEX" height="50px" style="margin: 0 20px;">
        <img src="https://tukuz.com/wp-content/uploads/2020/12/japan-exchange-group-jpx-logo-vector.png" alt="JPX" height="110px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwc6CEIT7viFT9bnP4OWFlKTEQw4-J2AaWGw&s" alt="KRX" height="40px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/New_Euronext_logo.svg/2560px-New_Euronext_logo.svg.png" alt="EURONEXT" height="70px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/London_Metal_Exchange_logo.svg/2560px-London_Metal_Exchange_logo.svg.png" alt="LME" height="60px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Cboe_Global_Markets_Logo.svg/2560px-Cboe_Global_Markets_Logo.svg.png" alt="CBOE" height="40px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/90/ICE_logo_100px_RGB-01.png" alt="ICE" height="80px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/NYSE_Logo_2022.svg/2560px-NYSE_Logo_2022.svg.png" alt="NYSE" height="45px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/CME_Group_Logo.svg/2560px-CME_Group_Logo.svg.png" alt="CME" height="30px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZAX5ZAEG5xFy8r9PYoHdLTqPbXWoUodYRJg&s" alt="EUREX" height="50px" style="margin: 0 20px;">
        <img src="https://companieslogo.com/img/orig/ASX.AX_BIG-a1970d7d.png?t=1720244490" alt="ASX" height="50px" style="margin: 0 20px;">
        <img src="https://22364887.fs1.hubspotusercontent-na1.net/hub/22364887/hubfs/VettaFi%20Logos/VettaFi_Logo_PURPLE_HEX.png?width=2035&height=484&name=VettaFi_Logo_PURPLE_HEX.png" alt="VettaFi" height="35px" style="margin: 0 20px;">
    </div>
</div>
"""
st.markdown(marquee_2, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""###### :blue-background[⭐ [Fintech] Domestic Platform Resources]""", help='[金融科技] 國內平台資源')
marquee_3 = """
<div style="width: 100%; overflow: hidden; white-space: nowrap; box-sizing: border-box; background-color: white; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
    <div style="display: inline-block; animation: marquee 20s linear infinite;">
        <img src="https://play-lh.googleusercontent.com/L1T5_zxxHgiBNF1ezwFKN5lbMFPqsYkLrijXyRb3Wg6lKsBL5FMjbQ7xI03zRjAy4mEX=w416-h235-rw" alt="臺灣證券交易所" height="120px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOTXAuhMkmlJiMDMlIJqsLKVJSiI-1nJb2KA&s" alt="臺灣證券櫃檯買賣中心" height="50px" style="margin: 0 20px;">
        <img src="https://www.taifex.com.tw/eventTryTryp7/resources/images/logo.png" alt="臺灣期貨交易所" height="50px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0wjj46ywbVgfFV1O5665CKcTHsw8lH0LasgeluoC__81PrdwEjExvfMGn_oNiiV9FvME&usqp=CAU" alt="臺灣集保結算所" height="80px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Opendata_gov_logo.png" alt="政府資料開放平台" height="60px" style="margin: 0 20px;">
        <img src="https://wwwap.bot.com.tw/ESG/img/logo.png" alt="台灣銀行" height="50px" style="margin: 0 20px;">
        <img src="https://s.yimg.com/os/creatr-uploaded-images/2022-01/6ebfe500-6d4a-11ec-bbff-abf6a43ba89d" alt="Yahoo_股市" height="60px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcv08Ao21Y4VwQxI8B0sswrVOPBy_XF-x-cA&s" alt="嗨投資" height="50px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/zh/thumb/9/95/Anue_logo.svg/1200px-Anue_logo.svg.png" alt="鉅亨網" height="40px" style="margin: 0 20px;">
        <img src="https://play-lh.googleusercontent.com/g9yFA_COUcRLk12o2UV40OjPASmojo9sY-WV-Wb7HuDa5DQvhxYwzP6xz-HiHTJyZA" alt="股市爆料同學會" height="80px" style="margin: 0 20px;">
        <img src="https://www.moneydj.com/funddj/images/FB-News.png" alt="moneydj" height="90px" style="margin: 0 20px;">
        <img src="https://corp.pchome.tw/wp-content/uploads/2021/08/6-1.png" alt="pchome" height="30px" style="margin: 0 20px;">
        <img src="https://play-lh.googleusercontent.com/L1T5_zxxHgiBNF1ezwFKN5lbMFPqsYkLrijXyRb3Wg6lKsBL5FMjbQ7xI03zRjAy4mEX=w416-h235-rw" alt="臺灣證券交易所" height="120px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOTXAuhMkmlJiMDMlIJqsLKVJSiI-1nJb2KA&s" alt="臺灣證券櫃檯買賣中心" height="50px" style="margin: 0 20px;">
        <img src="https://www.taifex.com.tw/eventTryTryp7/resources/images/logo.png" alt="臺灣期貨交易所" height="50px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0wjj46ywbVgfFV1O5665CKcTHsw8lH0LasgeluoC__81PrdwEjExvfMGn_oNiiV9FvME&usqp=CAU" alt="臺灣集保結算所" height="80px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7f/Opendata_gov_logo.png" alt="政府資料開放平台" height="60px" style="margin: 0 20px;">
        <img src="https://wwwap.bot.com.tw/ESG/img/logo.png" alt="台灣銀行" height="50px" style="margin: 0 20px;">
        <img src="https://s.yimg.com/os/creatr-uploaded-images/2022-01/6ebfe500-6d4a-11ec-bbff-abf6a43ba89d" alt="Yahoo_股市" height="60px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcv08Ao21Y4VwQxI8B0sswrVOPBy_XF-x-cA&s" alt="嗨投資" height="50px" style="margin: 0 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/zh/thumb/9/95/Anue_logo.svg/1200px-Anue_logo.svg.png" alt="鉅亨網" height="40px" style="margin: 0 20px;">
    </div>
</div>
"""
st.markdown(marquee_3, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""###### :blue-background[⭐ [Fintech] Domestic Investment Credit]""", help='[金融科技] 國內所有投信資源')
marquee_4 = """
<div style="width: 100%; overflow: hidden; white-space: nowrap; box-sizing: border-box; background-color: white; padding: 10px; border-radius: 10px; border: 1px solid #ddd;">
    <div style="display: inline-block; animation: marquee 22s linear infinite;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYQrMv4_HmA6eV2W5sMTgFuYQn6JZD7uoMtA&s" alt="元大投信" height="40px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-dvMeYe12nD6mhm-_8dL1i2hCB4rC9Xktcg&s" alt="國泰投信" height="35px" style="margin: 0 20px;">
        <img src="https://www.sinotrade.com.tw/ec/20190709/assets/img/logo-02.png" alt="群益投信" height="70px" style="margin: 0 20px;">
        <img src="https://pic.pimg.tw/eventblog/1616750628-3142178197-g_n.png" alt="中信投信" height="80px" style="margin: 0 20px;">
        <img src="https://www.megafunds.com.tw/iitweb/recommend/2020q1/images/LogoM1-01.png.png" alt="兆豐投信" height="70px" style="margin: 0 20px;">
        <img src="https://osaas.commerce.nccu.edu.tw/uploads/media/1c0799dff2946808b0f5d870492c56be.png" alt="永豐投信" height="60px" style="margin: 0 20px;">
        <img src="https://www.jkoam.com/assets/images/Logo.png" alt="街口投信" height="70px" style="margin: 0 20px;">
        <img src="https://osaas.commerce.nccu.edu.tw/uploads/media/15748360586.jpg" alt="復華投信" height="50px" style="margin: 0 20px;">
        <img src="https://retirego.pension.org.tw/images/partner/Investment-Trust/06-Franklin.png" alt="富蘭克林華美投信" height="50px" style="margin: 0 20px;">
        <img src="https://www.uobam.com.tw/static/media/logo.6558096f.png" alt="大華銀投信" height="40px" style="margin: 0 20px;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlofzS_7-NlYjEMCP5Yr1Yuqg4h-H57SyMHw&s" alt="新光投信" height="50px" style="margin: 0 20px;">
        <img src="https://www.anuefund.com/Upload/Files/FundBrand/logo-Fubon_20220920030437998435.png" alt="富邦投信" height="100px" style="margin: 0 20px;">
        <img src="https://fs-static-web-assets.s3.ap-northeast-1.amazonaws.com/images/market/brands/logo/logo_normal_ezmoney.png" alt="統一投信" height="70px" style="margin: 0 20px;">
        <img src="https://fs-static-web-assets.s3.ap-northeast-1.amazonaws.com/images/market/brands/logo/logo_normal_FSITC.png" alt="第一金投信" height="80px" style="margin: 0 20px;">
        <img src="https://fs-static-web-assets.s3.ap-northeast-1.amazonaws.com/images/market/brands/logo/logo_normal_TSIT.png" alt="台新投信" height="75px" style="margin: 0 20px;">
        <img src="https://fsv.cmoney.tw/cmstatic/notes/coauthor/817.png" alt="野村投信" height="100px" style="margin: 0 20px;">
    </div>
</div>
"""
st.markdown(marquee_4, unsafe_allow_html=True)

csv_style = """
<style>
@keyframes marquee {
    0% { transform: translateX(110%); }
    100% { transform: translateX(-400%); }
}
</style>"""
st.markdown(csv_style, unsafe_allow_html=True)


st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)