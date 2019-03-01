from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from better_than_this.auth import login_required
from better_than_this.db import get_db

bp = Blueprint('location', __name__)

@bp.route('/')
def index():

    return render_template('location/index.html')