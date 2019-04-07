from better_than_this.external.yelp_client import businesses_search_suggestions


search_result={
  'categories': [
    {'title': 'Korean', 'alias': 'korean'},
    {'title': 'Asian Fusion', 'alias': 'asianfusion'},
    {'title': 'Fast Food', 'alias': 'hotdogs'}
  ],
  'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/qWvc9CWnFFTrWTo3dTMwbQ/o.jpg',
  'id': 'dT29Lc-VVb8EQ9b78ztTLA',
  'price': '$$$$',
  'request_duration': 0.031042999999999932,
  'address': '599 6th Ave \n New York, 10011',
  'name': 'Gogi Grill - Chelsea'
}

better_restaurants = businesses_search_suggestions(search_result)
print(better_restaurants)