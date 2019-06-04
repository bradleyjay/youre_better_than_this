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

