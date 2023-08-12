# from web3 import Web3

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



original_event_description = "Transfer (index_topic_1 address from, index_topic_2 address to, uint256 value)"

# 移除额外的文本，并替换参数名称
simplified_event_description = original_event_description.replace("index_topic_1 ", "").replace("index_topic_2 ", "")

print("Simplified Event Description:", simplified_event_description)

