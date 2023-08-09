# your_app/tasks.py

import requests
from airtable import Airtable
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings


def update_coin_details():
    coin_dict = {}
    # CoinGecko API endpoint
    coin_gecko_url = "https://api.coingecko.com/api/v3/coins/list"
    # Retrieve coin data from CoinGecko
    response = requests.get(coin_gecko_url)
    if response.status_code > 299 or response.status_code < 200:
        # We were either rate limited or some other error
        return
    
    coin_data = response.json()
    coin_data=coin_data[:20]

    # Initialize AirTable API
    airtable = Airtable(settings.AIRTABLE_BASE_ID, 'Coins', api_key=settings.AIRTABLE_ACCESS_KEY)

    # Update coin details in AirTable
    ids=[]

    for coin in coin_data:
        coin_id=coin['id']
        coin_dict[coin_id] = coin
        ids.append(coin_id)


    coin_gecko_url2 = "https://api.coingecko.com/api/v3/simple/price"
    response = requests.get(coin_gecko_url2, params={'ids': ','.join(ids), 'vs_currencies': 'usd'})
    if response.status_code > 299 or response.status_code < 200:
    # We were either rate limited or some other error
        return
    coin_data2 = response.json()
    print(coin_data2)

    for coin in coin_data2:
        if "usd" in coin_data2[coin]:
            coin_dict[coin]['price'] = coin_data2[coin]['usd']
            # Update or create the record in AirTable
            airtable.insert({"coin_id": coin,
                            "name": coin_dict[coin]["name"],
                            "price": str(coin_dict[coin]["price"]),
                            "symbol": coin_dict[coin]["symbol"]
                            })
    print("Created records!")

def price_update():
    #fetch from airtable
    airtable = Airtable(settings.AIRTABLE_BASE_ID, 'Coins', api_key=settings.AIRTABLE_ACCESS_KEY)
    records = airtable.get_all()
    coin_dict = {}
    for record in records:
        coin_dict[record['fields']['id']] = record['fields']['price']
    coin_gecko_url2 = "https://api.coingecko.com/api/v3/simple/price"
    response = requests.get(coin_gecko_url2, params={'ids': ','.join(coin_dict.keys()), 'vs_currencies': 'usd'})
    coin_data2 = response.json()
    if response.status_code > 299 or response.status_code < 200:
        # We were either rate limited or some other error
        return
    for coin in coin_data2:
        if coin_dict[coin] != coin_data2[coin]['usd']:
            coin_dict[coin] = coin_data2[coin]['usd']
            airtable.match("coin_id", coin)


scheduler = BackgroundScheduler()