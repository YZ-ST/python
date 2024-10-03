# 定義 API URLs
BLOCK = [
    'https://apilist.tronscanapi.com/api/block?sort=-balance&start=0&limit=20&producer=&number=&start_timestamp=&end_timestamp=',
    'https://apilist.tronscanapi.com/api/block/statistic'
]

TOKEN = [
    'https://apilist.tronscanapi.com/api/tokens/overview?start=0&limit=2&verifier=all&order=desc&filter=top&sort=&showAll=1&field=',
    'https://apilist.tronscanapi.com/api/token_trc20?contract=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&showAll=1&start=&limit='
]

MODULE = {'block': BLOCK, 'token': TOKEN}