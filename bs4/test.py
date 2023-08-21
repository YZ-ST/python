import requests
from bs4 import BeautifulSoup
from loguru import logger
import time
import re
import csv

logger.add("./log/log_{time}.log")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}
first_index = 63200
# 创建CSV文件并写入标题行
with open('Tron_contract_address.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'symbol', 'contract_address', 'decimal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for current_page_index in range(1265, 1559):
        logger.debug(f"current_page_index: {current_page_index}")
        url = f"https://apilist.tronscanapi.com/api/tokens/overview?start={first_index}&limit=50&verifier=all&order=desc&filter=trc20&sort=init&order_current=descend"
        symbol_response = requests.get(url, headers=headers)
        symbol_info = symbol_response.json()
        symbol_info = symbol_info["tokens"]

        for symbol in symbol_info:
            name = symbol["name"]
            symbol_abbr = symbol["abbr"]
            contract_address = symbol["contractAddress"]
            decimal = symbol["decimal"]
            logger.debug(f"name: {name}, symbol: {symbol_abbr}, contract_address: {contract_address}, decimal: {decimal}")

            # 将数据写入CSV文件
            writer.writerow({
                'name': name,
                'symbol': symbol_abbr,
                'contract_address': contract_address,
                'decimal': decimal
            })

        first_index += 50