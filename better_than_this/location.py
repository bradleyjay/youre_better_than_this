from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from better_than_this.auth import login_required
from better_than_this.db import get_db
from better_than_this.http_funcs import get_restaurant   #handles api call and resp

bp = Blueprint('location', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():    
    if request.method == 'POST':
        # unpack the name, address fields
        # using the "name" field from templates/locations/index.html
        name = request.form['name'] 
        address = request.form['address']

       # test via PRINT
        print(name)
        print(address)
        
        # send this data to Yelp API
        search_result = get_restaurant(name, address)
        print(search_result)

    return render_template('location/index.html')