import datetime as dt
import pandas as pd
import requests

yesterday = dt.date.today() - dt.timedelta(days=1)
api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
payload = {
    'format': 'geojson',
    'starttime': yesterday - dt.timedelta(days=30),
    'endtime': yesterday
}
response = requests.get(api, params=payload)
earthquake_response = response.json()
print(earthquake_response.keys())

print(earthquake_response['bbox'])


earthquake_properties = [
    quake['properties']
    for quake in earthquake_response['features']
]

df = pd.DataFrame(earthquake_properties)

print(df)
