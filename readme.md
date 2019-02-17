# You're Better Than This

App to improve your taste. 

High level, user exp:
1) User fills out webform with a restaurant they like, and a location.
...
4) App returns similar but better restaurants near the address, again via Yelp API. Just a list.


What the app does:
1) User enters a restaurant they like, and a location.
- in a form, generate the info that we'll send to the API request
<!-- 2) App confirms the location is real via Google Maps API (or similar) [might not need this, Yelp might know]
2a) If real, commit to database. Else, ask user again (maybe with suggestion "did you mean?") -->


3) Get info on entered restaurant
3a) App grabs data from Yelp API on the restaurant (via the form data)
3b) Return a form for user, with hidden field = yelp restaurant ID. Show Name, Display address of the restaurant
- Ask the user if restaurant match - yes? Repeat API call, now with yelp restaurant ID, then parse
- No match? Ask user again

4) From the Yelp API response, parse for only the data we want from the packet:
- Rating
- id (unique identifier)
- name
- display address
- categories (could either go bar/restaurant table + categories table with a bridge table in between; OR save these for this one request (how?))

5) Hit the API to recommend better restaurnts. With magic.

Extension Later:
- could save those categories, use the bigger table design (restaurnt + category tables, bridge)
- cache the initial APi response in its own cache db, when confirmed, dump that into storage db

Next steps: 
- user login (user db too)
- "Search restaurnt form"
- Yelp adapter and parser
