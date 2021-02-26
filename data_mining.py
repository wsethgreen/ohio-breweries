import requests
import json
import pandas as pd


# Base API Call url
api_url = 'https://api.openbrewerydb.org/breweries/search?query=ohio'

# Call API
beer_json_data = requests.get(api_url).json()

# Create Dictionary to house Ohio Breweries data

ohio_brew = {
    'id': [],
    'name': [],
    "brewery_type": [],
    "street": [],
    "city": [],
    "state": [],
    "postal_code": [],
    "longitude": [],
    "latitude": [],
    "phone": [],
    "website_url": [],
    }

# Create a dictionary to house the breweries who don't have lats/longs

ohio_brew_no_geo = {
    'id': [],
    'name': [],
    "brewery_type": [],
    "street": [],
    "city": [],
    "state": [],
    "postal_code": [],
    "longitude": [],
    "latitude": [],
    "phone": [],
    "website_url": [],
    }

# Extract data from json and add it to dictionary

for record in beer_json_data:
    if record['state'] == 'Ohio' and record['latitude'] != None:
        ohio_brew['id'].append(record['id'])
        ohio_brew['name'].append(record['name'])
        ohio_brew['brewery_type'].append(record['brewery_type'])
        ohio_brew['street'].append(record['street'])
        ohio_brew['city'].append(record['city'])
        ohio_brew['state'].append(record['state'])
        ohio_brew['postal_code'].append(record['postal_code'])
        ohio_brew['longitude'].append(record['longitude'])
        ohio_brew['latitude'].append(record['latitude'])
        ohio_brew['phone'].append(record['phone'])
        ohio_brew['website_url'].append(record['website_url'])
    if record['state'] == 'Ohio' and record['latitude'] == None:
        ohio_brew_no_geo['id'].append(record['id'])
        ohio_brew_no_geo['name'].append(record['name'])
        ohio_brew_no_geo['brewery_type'].append(record['brewery_type'])
        ohio_brew_no_geo['street'].append(record['street'])
        ohio_brew_no_geo['city'].append(record['city'])
        ohio_brew_no_geo['state'].append(record['state'])
        ohio_brew_no_geo['postal_code'].append(record['postal_code'])
        ohio_brew_no_geo['longitude'].append(record['longitude'])
        ohio_brew_no_geo['latitude'].append(record['latitude'])
        ohio_brew_no_geo['phone'].append(record['phone'])
        ohio_brew_no_geo['website_url'].append(record['website_url'])
        
# Convert dictionaries to dfs

ohio_brew_df = pd.DataFrame.from_dict(ohio_brew)
ohio_brew_no_geo_df = pd.DataFrame.from_dict(ohio_brew_no_geo)

# Convert the latitudes and longitudes to floats

ohio_brew_df['latitude'] = ohio_brew_df['latitude'].apply(lambda x: float(x))
ohio_brew_df['longitude'] = ohio_brew_df['longitude'].apply(lambda x: float(x))

# Reformat phone numbers so they are easier to read

def phone_format(phone):
    if len(phone) > 1:
        area_code = phone[0:3]
        first_3 = phone[3:6]
        last_4 = phone[-4:]
        return area_code + '-' + first_3 + '-' + last_4
    else:
        return 'n/a'

ohio_brew_df['phone'] = ohio_brew_df['phone'].apply(lambda x: phone_format(x))
ohio_brew_no_geo_df['phone'] = ohio_brew_no_geo_df['phone'].apply(lambda x: phone_format(x))

# Update website urls so they are https rather than http

def url_format(url):
    if len(url) > 1:
        http = url[0:4]
        domain = url[4:]
        return http + 's' + domain
    else:
        return 'n/a'

ohio_brew_df['website_url'] = ohio_brew_df['website_url'].apply(lambda x: url_format(x))
ohio_brew_no_geo_df['website_url'] = ohio_brew_no_geo_df['website_url'].apply(lambda x: url_format(x))

