"""
Contains functions for grabbing data and parsing it, from the Yelp API
"""

import http.client

def get_restaurant(name, address):
    conn = http.client.HTTPSConnection("api.yelp.com")   # no trailing slash!!

    # HTTPConnection.request(method, url, body=None, headers={}, *, encode_chunked=False)
    # parser wil have to build params into our URL

    headers = {'Authorization': 'Bearer API_KEY'}
    conn.request('GET', '/v3/businesses/search?term=Faro&location=NYC', headers=headers) #URL must start with / (?)

    r1 = conn.getresponse()
    
    # .read() gives us the HTTP body response back - we'll need to parse this,
    # dig out just the name of the restaurant and it's street address, maybe
    # something else identifying too?
    answer = [r1.status, r1.reason, r1.read()]

    return answer