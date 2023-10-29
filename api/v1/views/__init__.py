#!/usr/bin/python3
"""
API views for flask app v1.
"""

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
<<<<<<< HEAD
=======
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
>>>>>>> 8fc6826526df2a8cfc0977df0820257058fe2b6e
