import datetime as dt
import pandas as pd
import requests

def make_request(endpoint, payload = None):
    return requests.get(
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/'f'{endpoint}',
        headers={'token':'eeghapwNFmidphXskJJqPefOGbzwjrlU'},
        params=payload
    )

response = make_request('datatypes')

print(response.json()['results'])

print([(data['id'], data['name']) for data in response.json()['results']])






