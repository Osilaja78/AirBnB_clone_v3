#!/usr/bin/python3
"""Index file for api views"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the API status"""

    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def stats():
    """Returns count for all classes"""

    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }

    obj_count = {}
    for cls in classes:
        obj_count[cls] = storage.count(classes[cls])
    
    return jsonify(obj_count)
