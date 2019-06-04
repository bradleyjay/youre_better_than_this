import pytest
import requests
from flask import g, session
from better_than_this.db import get_db
from support.fixtures import Test_Fixtures


yelp_response = Test_Fixtures.yelp_response


def test_new(client, app):
    assert client.get('/locations/new').status_code == 200


def test_verify(client, app, requests_mock):
    requests_mock.get('https://api.yelp.com/v3/businesses/search?term=faro&location=NYC', json=yelp_response)
    
    response = client.post(
        '/locations/verify', data={'name': 'faro', 'address': 'NYC'}
    )
    assert response.status_code == 200


def test_get_index(client, app, requests_mock):
    response = client.get('/locations')

    assert response.status_code == 302

    assert response.headers['Location'] == 'http://localhost/locations/new'

def test_post_index(client, app, requests_mock):
    requests_mock.get('https://api.yelp.com/v3/businesses/search?location=7+Carmine+St+%0A+New+York%2C+10014&radius=800&limit=5&sort_by=rating&price=1%2C+2&categories=pizza', json=yelp_response)
    

    search_result = {'name': "Joe's Pizza", 'address': '7 Carmine St \n New York, 10014', 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/FhbFkrh_3TrAOZvoWTyOJA/o.jpg', 'id': 'uc5qQMzs96rzjK27epDCug', 'categories': [{'alias': 'pizza', 'title': 'Pizza'}], 'price': '$', 'request_duration': 0.5822188854217529}
    

    response = client.post(
        '/locations', data={'search_result': str(search_result)}
    )
    
    assert response.status_code == 200



