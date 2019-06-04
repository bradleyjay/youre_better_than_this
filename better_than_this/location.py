from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import ast

from better_than_this.auth import login_required
from better_than_this.db import get_db
from better_than_this.external.yelp_client import (
    get_better_restaurants, get_restaurant
)

bp = Blueprint('location', __name__, url_prefix='/locations')

@bp.route('/verify', methods=('GET', 'POST'))
def verify():
    if request.method == 'POST':
        # unpack the name, address fields
        # using the "name" field from templates/locations/index.html
        name = request.form['name']
        address = request.form['address']

        # send this data to Yelp API
        search_result = get_restaurant(name, address)
        print(search_result)
        return render_template('location/verify.html', search_result=search_result)



@bp.route('/new')
def new():
    return render_template('location/new.html') # rename template for new

# @bp.route('', methods=['POST'])
@bp.route('', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        search_result = request.form['search_result']
        # Need to use ast.literal_eval because it seems this info coming back from the front end isn't technically json? Using this instead of json.load in the API
        # https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
        search_result = ast.literal_eval(search_result)

        better_restaurants = get_better_restaurants(search_result)

        flash(better_restaurants)
        return render_template('location/better_options.html', better_restaurants=better_restaurants)

    return redirect(url_for('location.new'))
     # rename template for new
