import pytest
import requests
from flask import g, session
from better_than_this.db import get_db

yelp_response = str({'coordinates': {'latitude': 40.707407, 'longitude': -73.922839}, 'categories': [{'title': 'Italian', 'alias': 'italian'}], 'rating': 4.0, 'review_count': 241, 'distance': 6028.260197370216, 'phone': '+17183818201', 'image_url': 'https://s3-media4.fl.yelpcdn.com/bphoto/uE_e7ROScbFLYLN2TVVViQ/o.jpg', 'location': {'address2': '', 'address3': '', 'state': 'NY', 'display_address': ['436 Jefferson St', 'Brooklyn, NY 11237'], 'address1': '436 Jefferson St', 'zip_code': '11237', 'country': 'US', 'city': 'Brooklyn'}, 'alias': 'faro-brooklyn', 'is_closed': False, 'price': '$$$', 'transactions': [], 'url': 'https://www.yelp.com/biz/faro-brooklyn?adjust_creative=VgYdbrJG3V8WxnE29HVmwQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=VgYdbrJG3V8WxnE29HVmwQ', 'display_phone': '(718) 381-8201', 'id': 'clOFor0bFSjse7EUfdRacg', 'name': 'Faro'})

# def test_new(client, app):
#     assert client.get('/locations/new').status_code == 200

# def test_verify(client, app, requests_mock):
#     requests_mock.get('http://api.yelp.com/v3/businesses/search?name=faro&term=NYC', text=yelp_response)
#     response = client.post(
#         '/locations/verify', data={'name': 'faro', 'address': 'NYC'}
#     )

#     assert 'http://localhost/locations/verify' == response.headers['Location']

