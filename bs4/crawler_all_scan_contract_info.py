import requests
from bs4 import BeautifulSoup
from loguru import logger
import time
import re
import csv
import json

class CrawlerAllscanContractInfo:
    @staticmethod
    def get_etherscan_contract_info():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        with open("Ethereum_contract_address.csv", "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["name", "symbol", "contract_address", "decimal"])

            for page_index in range(1, 26):
                logger.debug(f"current_page_index: {page_index}")
                # get token list by page index
                url = f"https://etherscan.io/tokens?p={page_index}"
                response = requests.get(url, headers=headers)

                for token_index in range(1, 51):
                    # parser html content by selector
                    soup = BeautifulSoup(response.text, "html.parser")
                    token_name = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a > div > div")
                    name = token_name[0].text
                    logger.debug(f"token_name: {name}")

                    token_symbol = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a > div > span")
                    symbol = token_symbol[0].text
                    symbol = re.search(r'\((.*?)\)', symbol).group(1)
                    logger.debug(f"symbol: {symbol}")

                    token_address = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a")

                    token_address = "0x" + token_address[0].get("href").split("0x")[1]

                    logger.debug(f"token_address: {token_address}")

                    url = f"https://etherscan.io/token/{token_address}"

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
                    csv_writer.writerow([name, symbol, token_address, decimal])

    @staticmethod
    def get_bscscan_contract_info():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        with open("BSC_contract_address_1.csv", "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["name", "symbol", "contract_address", "decimal"])

            for page_index in range(1, 26):
                logger.debug(f"current_page_index: {page_index}")
                # get token list by page index
                url = f"https://bscscan.com/tokens?p={page_index}"
                response = requests.get(url, headers=headers)
                for token_index in range(1, 51):
                    # parser html content by selector
                    soup = BeautifulSoup(response.text, "html.parser")
                    token_name = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a > div > div")
                    name = token_name[0].text
                    logger.debug(f"token_name: {name}")

                    token_symbol = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a > div > span")
                    symbol = token_symbol[0].text
                    symbol = re.search(r'\((.*?)\)', symbol).group(1)
                    logger.debug(f"symbol: {symbol}")

                    token_address = soup.select(
                        f"#ContentPlaceHolder1_tblErc20Tokens > table > tbody > tr:nth-child({token_index}) > td:nth-child(2) > a")

                    token_address = "0x" + token_address[0].get("href").split("0x")[1]

                    logger.debug(f"token_address: {token_address}")

                    url = f"https://bscscan.com/token/{token_address}"

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
                    csv_writer.writerow([name, symbol, token_address, decimal])
    
    @staticmethod
    def get_tronscan_contract_info():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        first_index = 0
        # 创建CSV文件并写入标题行
        with open('Tron_contract_address_11.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'symbol', 'contract_address', 'decimal']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            # 从第一页开始爬取到最後一页
            for current_page_index in range(1, 1559):
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
    @staticmethod
    def csv_to_json(csv_file, json_file):
        data = []
        with open(csv_file, "r", newline="", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                data.append(row)

        with open(json_file, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    logger.add("./log/log_{time}.log")
    # CrawlerAllscanContractInfo.get_etherscan_contract_info()
    # CrawlerAllscanContractInfo.get_bscscan_contract_info()
    # CrawlerAllscanContractInfo.get_tronscan_contract_info()
    csv_file = "BSC_contract_address.csv"
    json_file = "BSC_contract_address.json"
    CrawlerAllscanContractInfo.csv_to_json(csv_file, json_file)
