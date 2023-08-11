import requests
from bs4 import BeautifulSoup
import re
import csv
import os

network = "ethereum"


# 创建一个空的列表来存储所有的数据
contracts = []

with open('ethereum_contract_address.csv', 'r') as file:
    # 使用csv.reader读取文件内容
    reader = csv.reader(file)
    for row in reader:
        symbol, contract_address = row
        contracts.append((symbol, contract_address))

# 从列表中提取第一个元素的数据
print(contracts)

# 使用for循环遍历contracts列表，提取并打印每个元素的symbol和contract_address
for symbol, contract_address in contracts:
    print("symbol =", symbol)
    print("contract_address =", contract_address)

    # 目标网页的URL
    url = f"https://ethervm.io/decompile/{contract_address}"

    # 发起GET请求并获取网页内容
    response = requests.get(url)

    # 检查响应状态码，确保请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.content, "html.parser")

        # 查找带有指定属性的<div>标签
        specified_div = soup.find('div', {'data-server-rendered': "true"})
        content = specified_div.get_text()

        # 使用正则表达式提取指定内容
        match = re.search(r'4byte\.directory\.(.*?)returns \(r0\)', content, re.DOTALL)
        extracted_text = match.group(1).strip()

        # 使用正則表達式找到所有的 "0x" 開頭到 "0x" 之前結束的部分
        matches = re.findall(r'0x.*?(?=0x|$)', extracted_text)


        # 判斷文件是否已存在，若不存在則寫入標題
        if not os.path.exists('data.csv'):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["network", "symbol", "contract_address","method_ID", "method"])

        # 輸出結果
        for match in matches:
            # 使用正則表達式找到 "Internal" 之前的所有內容
            result = re.split(r'Internal', match)[0].strip()
            
            # 分割方法ID和方法名稱
            parts = result.split(' ', 1)  # 將字符串分割成兩部分
            method_ID = parts[0].strip()  # 第一部分是方法ID
            method = parts[1].strip() if len(parts) > 1 else ""  # 第二部分是方法名稱（如果存在的話）


            # 將數據存入一個列表中
            data = [network, symbol, contract_address, method_ID, method]

            # 使用附加模式寫入數據
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
    else:
        print("请求失败，状态码:", response.status_code)
print("數據已成功寫入CSV文件!")