from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from better_than_this.auth import login_required
from better_than_this.db import get_db

bp = Blueprint('location', __name__)

@bp.route('/')
def index():    
    if request.method == 'POST':
        # unpack the name, address fields
        # using the "name" field from templates/locations/index.html
        name = request.form['name'] 
        address = request.form['address']

        # send this data to Yelp API

        

    return render_template('location/index.html')