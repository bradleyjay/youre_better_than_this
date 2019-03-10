"""
Contains functions for grabbing data and parsing it, from the Yelp API
"""

import http.client
import urllib
import json
import os

def get_restaurant(name, address):
    restaurants = businesses_search(name, address)
    if restaurants:
        return restaurants['businesses'][0]
    else:
        return 'things have gone badly'

def businesses_search(name, address):
    conn = http.client.HTTPSConnection("api.yelp.com")


    headers = {'Authorization': 'Bearer ' + os.environ['YELP_API_KEY']}
    conn.request('GET', generate_url(name, address), headers=headers)

    response = conn.getresponse()

    # .read() gives us the HTTP body response back - we'll need to parse this,
    # dig out just the name of the restaurant and it's street address, maybe
    # something else identifying too?
    if response.status == 200:
        return decode_body_response(response)
    else:
        return false

def decode_body_response(response):
    byte_body = response.read()
    string_body = byte_body.decode("utf-8")
    json_body = json.loads(string_body)
    return json_body

def generate_url(name, address):
    query_params = {'term' : name, 'location' : address}
    return '/v3/businesses/search?' + urllib.parse.urlencode(query_params)
