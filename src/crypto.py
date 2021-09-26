from pycoingecko import CoinGeckoAPI
def takecoi():
    coin = CoinGeckoAPI()
    print("Input number of coins ")
    x = int(input())
    data = coin.get_coins_markets( vs_currency="usd", per_page=x)
    for i in range(x):
        print(data[i].get('name'))