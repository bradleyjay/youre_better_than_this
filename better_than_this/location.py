from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from better_than_this.auth import login_required
from better_than_this.db import get_db
from better_than_this.external.yelp_client import get_restaurant
from better_than_this.external.yelp_client import businesses_search_suggestions   #handles api call and resp

bp = Blueprint('location', __name__, url_prefix='/locations')

@bp.route('/verify', methods=('GET', 'POST'))
def verify():
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
        return render_template('location/verify.html', search_result=search_result)

    

@bp.route('/new')
def new():
    

    return render_template('location/new.html') # rename template for new

@bp.route('', methods=['POST'])
def index():
    if request.method == 'POST':



        flash("Success!")

        # second api call goes here for more detail

        better_restaurants = businesses_search_suggestions(search_result)
        print(better_restaurants)

    return redirect(url_for('location.new'))
     # rename template for new