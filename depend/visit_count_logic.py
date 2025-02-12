import os, json, requests, gspread
from google.oauth2 import service_account

def visit_count(update_col: str) -> int:
    # """
    # Google Sheet 欄位格式
    # 1 Page(A) Name(B) Count(C)
    # 2 1 Home 0
    # 3 2 My Project 0
    # 4 3 Experience with Web Crawler 0
    # 5 4 Use LineBot Connecting GenAI 0
    # 6 5 Stock Heatmap 0
    # 7 6 Stream Discounts Items 0
    # 8 7 Simulated Trading System 0
    # """

    # 設定 Google Sheets API
    SHEET_ID = "1hwF4D_wlJ6QVh0t79oBagx8ybLrPFi81wsotj_cSpJ8"
    gist_url = f'https://gist.github.com/Junwu0615/{os.environ.get('VISIT_COUNT_ID')}'
    res = requests.get(f"{gist_url}/raw")
    loader = json.loads(res.text)

    # 連接 Google Sheets
    creds = service_account.Credentials.from_service_account_info(loader, scopes=['https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)

    # 開啟 Google Sheets
    sheet = client.open_by_key(SHEET_ID).sheet1

    # 讀取當前訪客次數
    visit_count = sheet.acell(update_col).value  # 取得儲存格的值
    visit_count = int(visit_count) + 1
    sheet.update(update_col, [[visit_count]]) # 更新 Google Sheets

    return visit_count