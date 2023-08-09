

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings
from airtable import Airtable

@api_view(['GET'])
def get_coins(request):
    airtable = Airtable(settings.AIRTABLE_BASE_ID, 'Coins', api_key=settings.AIRTABLE_ACCESS_KEY)
    records = airtable.get_all()
    print(records)
    response = {}
    for record in records:
        print(record)
        if "coin_id" in record["fields"]:
            response["coin_id"] = record["fields"]
    
    return Response(response, status=200)


@api_view(['GET'])
def get_coinprice(request, coinId):
    # Get coin from airtable
    airtable = Airtable(settings.AIRTABLE_BASE_ID, 'Coins', api_key=settings.AIRTABLE_ACCESS_KEY)
    record = airtable.get(coinId)

    return Response({"coins": 10})
