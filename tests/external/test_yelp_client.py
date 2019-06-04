import pytest
import os
import requests
from better_than_this.external.yelp_client import get_restaurant, get_better_restaurants
from support.fixtures import Test_Fixtures


yelp_response = Test_Fixtures.yelp_response


## Tests for get_restaurant, get_better_restaurants

def test_get_restaurant(requests_mock):
    requests_mock.get('https://api.yelp.com/v3/businesses/search?term=faro&location=nyc', json=yelp_response, status_code=200)

    response = get_restaurant('faro','nyc')

    restaurant_attrs = ['name', 'image_url', 'price', 'categories','address','id', 'request_duration']

    for restaurant_attr in restaurant_attrs:
        assert restaurant_attr in response


def test_get_better_restaurants(requests_mock):

    requests_mock.get('https://api.yelp.com/v3/businesses/search?radius=800&location=123+Fake+Street&categories=italian&price=2%2C+3%2C+4&limit=5&sort_by=rating', json=yelp_response, status_code=200)


    search_results = {
            "name": "Faro",
            "address": "123 Fake Street",
            "image_url": "www.image.com",
            "id": "12345",
            "categories": [{'title': 'Italian', 'alias': 'italian'}],
            "price": "$$$"
        }
    response = get_better_restaurants(search_results)

    restaurant_attrs = ['name', 'image_url', 'price', 'categories','address','id', 'request_duration']

    for restaurant in response:
        for restaurant_attr in restaurant:
            assert restaurant_attr in restaurant_attrs
