# server.py
from fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool()
def get_now_weather(city: str) -> dict:
    API_KEY = ""  # 請填寫自己申請的API KEY
    FORMAT = "JSON"
    LOCATION_NAME = city
    url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&format={FORMAT}&locationName={LOCATION_NAME}"
    response = requests.get(url)  # 取得 JSON 檔案的內容為文字

    if response.status_code == 200:
        data = response.json()
        return {
            "weather": data["records"]["location"][0]["weatherElement"][0]["time"][0][
                "parameter"
            ]["parameterName"]
        }


if __name__ == "__main__":
    mcp.run(transport="stdio")
