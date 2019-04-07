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
        return location_from_api(candidate, request_duration)

    return "ERROR - bad API response"

def get_better_restaurants(search_result):
    results, request_duration = businesses_search_suggestions(search_result)
    if results:
        return list(map(location_from_api, results["businesses"]))

    return "ERROR - bad API response"

def parse_location(location):
    return location["address1"] + " \n " + location["city"] + ", " + location["zip_code"]


def businesses_search(name, address):
    url = generate_url({"term": name, "location": address})
    return make_request(url)

def businesses_search_suggestions(search_result):
    query_params = {
        "location": search_result['address'],
        "radius": 800,
        "limit": 5,
        "sort_by": "rating",
        "price" : get_dollar_count(search_result["price"]),
        "categories" : get_categories(search_result["categories"])
    }
    url = generate_url(query_params)
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
        return False

def decode_body_response(response):
    byte_body = response.read()
    string_body = byte_body.decode("utf-8")
    json_body = json.loads(string_body)
    return json_body

def generate_url(query_params):
    return '/v3/businesses/search?' + urllib.parse.urlencode(query_params)

def get_dollar_count(price):
    dollar_count = len(price)

    if dollar_count==4:
        price_range = "3, 4"
    elif dollar_count==1:
        price_range = "1, 2"
    else:
        price_range = str(dollar_count-1) + ", " + str(dollar_count) + ", " + str(dollar_count + 1)

    return price_range

def get_categories(categories):
    mapped_categories = map(lambda category: category["alias"], categories)
    return ",".join(list(mapped_categories))

def location_from_api(businesses_data, request_duration=0):
    print("This is Business Data \n:" + str(businesses_data))

    if all (k in businesses_data for k in ("name", "location")):
        return {
            "name": businesses_data["name"],
            "address": parse_location(businesses_data["location"]),
            "image_url": businesses_data["image_url"],
            "id": businesses_data["id"],
            "categories": businesses_data["categories"],
            "price": businesses_data["price"],
            "request_duration": request_duration
        }
    else:
        return "Missing keys"
