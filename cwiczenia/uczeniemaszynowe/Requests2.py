import datetime as dt
import pandas as pd
import requests


def make_request(endpoint, payload=None):
    return requests.get(
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/'f'{endpoint}',
        headers={'token': 'eeghapwNFmidphXskJJqPefOGbzwjrlU'},
        params=payload
    )


def get_item(name, what, endpoint, start=1, end=None):
    """
    Grab the JSON payload for a given field by name using binary search.

    Parameters:
        - name: The item to look for.
        - what: Dictionary specifying what the item in `name` is.
        - endpoint: Where to look for the item.
        - start: The position to start at. We don't need to touch this, but the
                 function will manipulate this with recursion.
        - end: The last position of the items. Used to find the midpoint, but
               like `start` this is not something we need to worry about.

    Returns:
        Dictionary of the information for the item if found otherwise
        an empty dictionary.
    """
    # find the midpoint which we use to cut the data in half each time
    mid = (start + (end or 1)) // 2

    # lowercase the name so this is not case-sensitive
    name = name.lower()

    # define the payload we will send with each request
    payload = {
        'datasetid': 'GHCND',
        'sortfield': 'name',
        'offset': mid,  # we will change the offset each time
        'limit': 1  # we only want one value back
    }

    # make our request adding any additional filter parameters from `what`
    response = make_request(endpoint, {**payload, **what})

    if response.ok:
        payload = response.json()

        # if response is ok, grab the end index from the response metadata the first time through
        end = end or payload['metadata']['resultset']['count']

        # grab the lowercase version of the current name
        current_name = payload['results'][0]['name'].lower()

        # if what we are searching for is in the current name, we have found our item
        if name in current_name:
            return payload['results'][0]  # return the found item
        else:
            if start >= end:
                # if our start index is greater than or equal to our end, we couldn't find it
                return {}
            elif name < current_name:
                # our name comes before the current name in the alphabet, so we search further to the left
                return get_item(name, what, endpoint, start, mid - 1)
            elif name > current_name:
                # our name comes after the current name in the alphabet, so we search further to the right
                return get_item(name, what, endpoint, mid + 1, end)
    else:
        # response wasn't ok, use code to determine why
        print(f'Response not OK, status: {response.status_code}')


response = make_request('datasets', {'startDate': '2018-10-01'})

print(response.status_code)
payload = response.json()
print(response.json().keys())

print(payload['metadata'])
print(payload['results'][0].keys())

print([(data['id'], data['name']) for data in payload['results']])

response3 = make_request('datatypes', payload={'datacategoryid': 'TEMP', 'limit': 100})

warsaw = get_item('Warsaw', {'locationcategoryid': 'CITY'}, 'locations')
print(warsaw)
okecie = get_item('OKECIE, PL', {'locationid': warsaw['id']}, 'stations')
print('OKECIE')
print(okecie)

pogoda_na_okeciu = make_request(
    'data',
    {'datasetid': 'GHCND',
     'stationid': okecie['id'],
     'locationid': warsaw['id'],
     'startdate': '2018-10-01',
     'enddate': '2018-10-31',
     'datatypeid': ['TAVG', 'TMAX', 'TMIN'],
     'units': 'metric',
     'limit': 1000}
)
data_frame = pd.DataFrame(pogoda_na_okeciu.json()['results'])

print('data frame')
print(data_frame)
