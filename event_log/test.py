from web3 import Web3
import requests
from bs4 import BeautifulSoup
import csv
import os
# 將十六進制字串轉換為十進制整數
# def get_event_signature_hash(event_description):
#     # 创建 web3 实例
#     w3 = Web3()
#     # 计算事件签名的 Keccak-256 哈希
#     event_signature_hash = w3.solidity_keccak(["string"], [event_description])
#     return event_signature_hash.hex()

# # 事件描述
# event_description = "Transfer(address,address,uint256)"
# event_signature = get_event_signature_hash(event_description)
# print("Event Signature:", event_signature)


# 到etherscan指定要爬取的transacion log
network = "ethereum"
# 0x0a9d888ed9be6a12f2be10116de012061652f6bdc50e3c4614be4c1d8a51d1b3、
# 0x50648fa5a012b31e7ec32f974e4f464ac40d4ec6ee9b3291138635907f01b980、
# 0xece6b5bc85a12cab6f03ff8dd1f704187c56a3f6b2eaea9fbb7b88aadf3c7892、
# 0xa1794148e61713c6ecc2f8f5913d4b41f24eec243826820255252e2a6cdb3091、
# 0x1393dd521671cbad5c3e8283b9e1a9442f817697ccf95854aa53c1bad29b16f4
transaction_hash = '0x1393dd521671cbad5c3e8283b9e1a9442f817697ccf95854aa53c1bad29b16f4'
url = f"https://etherscan.io/tx/{transaction_hash}#eventlog"

# 发起HTTP GET请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)
print(response.status_code)

# 检查响应状态码是否为200 (成功)
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 尋找所有以 "funcname_" 开头的<span>元素
    method = []
    funcname_spans = soup.find_all("span", id=lambda x: x and x.startswith("funcname_"))
    # 提取并打印每个<span>元素的内容
    for span in funcname_spans:
        span_content = span.get_text(strip=True)
        modified_text = span_content.replace("View Source", "").strip()
        # print("Content:",modified_text)
        method.append(modified_text)

    
    # 寻找所有<span class="font-monospace text-break">元素
    span_elements = soup.find_all("ul", class_="list-unstyled list-xs-space fs-sm mb-0")
    topic = []
    for span in span_elements:
        # 提取span_elements裡所有的<li>元素的<class="font-monospace text-break">
        li_elements = span.find_all("li")
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(str(li_elements[0]), "html.parser")

        # 寻找第一个<span class="font-monospace text-break">元素
        span_element = soup.find("span", class_="font-monospace text-break")

        if span_element:
            span_content = span_element.get_text(strip=True)
            # print("Content inside span:", span_content)
            topic.append(span_content)
        else:
            print("No matching span element found.")

    # 將method和topic儲存為key-value pair
    method_topic = dict(zip(method, topic))
    print(method_topic)

    # 移除重複的value
    method_topic = {v: k for k, v in method_topic.items()}
    print(method_topic)

    # 指定要写入的CSV文件名
    csv_filename = "method_topic.csv"

    # 如果CSV文件不存在，则创建并写入表头
    if not os.path.exists(csv_filename):
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["network", "method", "topic"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    # 读取已存在的数据
    existing_methods = set()
    if os.path.exists(csv_filename):
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                existing_methods.add(row["topic"])

    # 将新数据写入CSV文件，仅写入不存在的数据
    with open(csv_filename, mode="a", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["network", "method", "topic"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for key, value in method_topic.items():
            if key not in existing_methods:
                writer.writerow({"network": network, "method": value, "topic": key})
                existing_methods.add(key)


    # # 将数据写入CSV文件，可以重複寫入
    # with open(csv_filename, mode="a", newline="", encoding="utf-8") as csv_file:
    #     fieldnames = ["network","method", "topic"]
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     # writer.writeheader()
    #     for key, value in method_topic.items():
    #         writer.writerow({"network":network,"method": key, "topic": value}) 
    # print(f"Data written to {csv_filename} successfully.")
else:
    print("Failed to retrieve the page.")