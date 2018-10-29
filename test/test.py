import requests
# url = 'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_INR/history?period_id=1MIN&time_start=2016-01-01T00:00:00'
# to get historical data.
url = 'https://rest.coinapi.io/v1/trades/BITSTAMP_SPOT_BTC_USD/history?time_start=2018-10-28T00:00:00'
headers = {'X-CoinAPI-Key' : '6C06802E-EDFF-46E0-A666-8BF50B773ABD'}
response = requests.get(url, headers=headers)
data = response.json()
print(data)
# print(str(response))