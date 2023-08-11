# import requests

# def get_contract_source(contract_address):
#     api_key = 'THKJZBN5T5N7Y9B4BSXPCQ4ZIV3VACC128'
#     base_url = 'https://api.etherscan.io/api'
    
#     params = {
#         'module': 'contract',
#         'action': 'getsourcecode',
#         'address': contract_address,
#         'apikey': api_key
#     }
    
#     response = requests.get(base_url, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         if data['status'] == '1' and data['result']:
#             ABI_code = data['result'][0]['ABI']
#             ABI_code = ABI_code.replace("true", "True")
#             ABI_code = ABI_code.replace("false", "False")
#             return ABI_code
#         else:
#             return "Error in retrieving source code. Message:", data.get('message', 'Unknown error')
#     else:
#         return f"Error in HTTP request. Status code: {response.status_code}"


# contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
# ABI_code = get_contract_source(contract_address)
# print(ABI_code)


# import ast
# ABI_code = '[{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]'
# contract_abi = ast.literal_eval(ABI_code)
# print(contract_abi)
# print(type(contract_abi))


import csv

# 创建一个空的列表来存储所有的数据
contracts = []

with open('ethereum_contract_address.csv', 'r') as file:
    # 使用csv.reader读取文件内容
    reader = csv.reader(file)

    # 跳过标题行（如果有的话）
    next(reader)

    for row in reader:
        symbol, contract_address = row
        contracts.append((symbol, contract_address))

# 从列表中提取第一个元素的数据
print(contracts)

# 使用for循环遍历contracts列表，提取并打印每个元素的symbol和contract_address
for symbol, contract_address in contracts:
    print("symbol =", symbol)
    print("contract_address =", contract_address)
    print()  # 打印空行以分隔每个条目


