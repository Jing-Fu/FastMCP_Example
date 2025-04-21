# 氣象查詢MCP伺服器

## 專案概述
本專案使用FastMCP框架建立氣象資料查詢服務，透過中央氣象署開放資料平台API取得即時天氣資訊。主要功能包含：
- 提供標準MCP協議接口
- 查詢台灣指定城市的天氣狀況
- 簡易的本地開發測試環境

## 快速安裝

### 安裝步驟

使用uv(https://github.com/astral-sh/uv)來建立虛擬環境
```bash

# 安裝依賴套件
uv pip install fastmcp requests
```


## 備註
氣象開發平台API註冊授權: https://opendata.cwa.gov.tw/user/authkey
