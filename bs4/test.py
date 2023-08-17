import requests
from bs4 import BeautifulSoup
from loguru import logger
import time
import re

token_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
url = f"https://etherscan.io/token/{token_address}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    # Add any other headers you might need
}
symbol_response = requests.get(url, headers=headers)
soup = BeautifulSoup(symbol_response.text, "html.parser")

decimal_html = soup.select(
    f"#ContentPlaceHolder1_divSummary > div.row.g-3.mb-4 > div:nth-child(3) > div > div > div:nth-child(2) > h4")

# get decimal_html type to string
decimal_html_to_string = str(decimal_html[0])
soup = BeautifulSoup(decimal_html_to_string, 'html.parser')
# 找到 <b> 標籤
b_tag = soup.find('b')
# 獲取 <b> 標籤內容
decimal = b_tag.get_text()
logger.debug(f"decimal: {decimal}")

