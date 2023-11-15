import json
# JSONファイルの読み込み
with open('catalog.json') as file:
    data = json.load(file)

# jacketの価格データを抽出
jacket_prices = [item['price'] for item in data if item['name'] == 'jacket']
jacket_count = sum(1 for item in data if item['name'] == 'jacket')

if jacket_prices:
    max_price = max(jacket_prices)
    min_price = min(jacket_prices)

    print(f"jacketの個数: {jacket_count}")
    print(f"jacketの最高価格: {max_price}")
    print(f"jacketの最低価格: {min_price}")
