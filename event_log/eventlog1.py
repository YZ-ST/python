from web3 import Web3
import requests
import ast
import binascii

def get_contract_abi(contract_address):
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
            ABI_code = ast.literal_eval(ABI_code)
            return ABI_code
        else:
            return "Error in retrieving source code. Message:", data.get('message', 'Unknown error')
    else:
        return f"Error in HTTP request. Status code: {response.status_code}"

def get_topic_argument_first(transaction_hash):
    receipt = w3.eth.get_transaction_receipt(transaction_hash)
    
    for log in receipt['logs']:
        first_topic = log['topics'][0]
        # 转换为十六进制字符串
        first_topic = '0x' + binascii.hexlify(first_topic).decode()
        # print("First HexBytes:", first_topic)
        return first_topic

if __name__ == '__main__':
    # 连接到以太坊节点
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/7a0cb58367f74af6bf2e4763404d0c8e'))

    transaction_hash = '0x7fbdef65611d3f22aefad53f4c6721574eecd3d2cde63bd960f587ac7e2f422c'
    
    first_topic = get_topic_argument_first(transaction_hash)
    print("First Topic:", first_topic)
