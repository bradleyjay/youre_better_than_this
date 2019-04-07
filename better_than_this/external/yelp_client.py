"""
Contains functions for grabbing data and parsing it, from the Yelp API
"""

import http.client
import urllib
import json
import os
import time

def get_restaurant(name, address):
    restaurants, request_duration = businesses_search(name, address) # remember, "return x, y" yields a tuple, which you unpack like so ^

    if restaurants:
        candidate = restaurants['businesses'][0]

        print(candidate)
        if all (k in candidate for k in ("name", "location")):
            print("got it.")
            return {
            "name": candidate["name"],
            "address": parse_location(candidate["location"]),
            "image_url": candidate["image_url"],
            "id": candidate["id"],
            "categories": candidate["categories"], # needs parsing fcn, API call will need comma seperated list
            "price": candidate["price"], #may need to be converted: $ -> 1, $$ -> 2, etc with fcn
            "request_duration": request_duration
            }

    return "ERROR - bad API response"

def parse_location(location):
    return location["address1"] + " \n " + location["city"] + ", " + location["zip_code"]


def businesses_search(name, address):
    url = generate_url({"term": name, "location": address})
    return make_request(url)

def businesses_search_suggestions(search_result):
    # TODO: Unpack location, price, and cat from search_result
    # query_params = {
    # "location": search_result["some_key"],
    # "radius": 800,
    # "open_now": True,
    # "limit": 5,
    # "sort_by": "rating",
    # "price" : search_result["price"],
    # "categories" : search_result["categories"]

    url = generate_url({"location": "NYC"}) # hardcoding for now
    return make_request(url)

def make_request(url):
    conn = http.client.HTTPSConnection("api.yelp.com")

    headers = {'Authorization': 'Bearer ' + os.environ['YELP_API_KEY']}

    # get request duration - wrap http call in clock times
    request_start = time.clock()
    conn.request('GET', url, headers=headers)
    request_duration = time.clock() - request_start

    response = conn.getresponse()

    if response.status == 200:
        return decode_body_response(response), request_duration
    else:
        return false

def decode_body_response(response):
    byte_body = response.read()
    string_body = byte_body.decode("utf-8")
    json_body = json.loads(string_body)
    return json_body

def generate_url(query_params):
    return '/v3/businesses/search?' + urllib.parse.urlencode(query_params)
