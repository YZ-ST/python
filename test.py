from web3 import Web3
import requests
import json
import ast
import csv

def get_contract_source(contract_address):
    api_key = 'THKJZBN5T5N7Y9B4BSXPCQ4ZIV3VACC128'
    base_url = 'https://api.etherscan.io/api'
    
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apikey': api_key
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and data['result']:
            ABI_code = data['result'][0]['ABI']
            ABI_code = ABI_code.replace("true", "True")
            ABI_code = ABI_code.replace("false", "False")
            return ABI_code
        else:
            return "Error in retrieving source code. Message:", data.get('message', 'Unknown error')
    else:
        return f"Error in HTTP request. Status code: {response.status_code}"


def get_methodID(input_data, contract_abi):
    w3 = Web3()
    # 創建合约對象
    contract = w3.eth.contract(abi=contract_abi)
    method_ID = input_data[:10]
    # print(f"method_ID = {method_ID}")
    # decode input data
    decoded_input = contract.decode_function_input(input_data)
    method = str(decoded_input[0])
    # 输出解码结果
    # print(f"method = {method}")
    return (method_ID, method)

if __name__ == '__main__':
    # 从Etherscan交易中获取的原始input data
    network = "ethereum"
    symbol = "USDT"
    input_data = "0xa9059cbb0000000000000000000000004cb68319704e889acac246b662d377db2a7ca277000000000000000000000000000000000000000000000000024fe77bffcb4075"
    contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
    
    # 合约的ABI
    contract_abi = get_contract_source(contract_address)
    contract_abi = ast.literal_eval(contract_abi)

    (method_ID, method) = get_methodID(input_data, contract_abi)
    print(method_ID)
    print(method)

    # 将数据写入CSV文件
    csv_file = "output.csv"

    # 将数据写入CSV文件
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["network", "symbol", "method_ID", "method"])
        writer.writerow([network, symbol, method_ID, method])

    print("Data written to", csv_file)