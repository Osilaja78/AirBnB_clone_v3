#!/usr/bin/python3
"""
Views for states objects.
"""


from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """Returns a list of all State object"""

    objs = []
    for obj in storage.all("State").values():
        objs.append(obj.to_dict())

    return jsonify(objs)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_with_id(state_id):
    """Returns a state with a specific id"""

    obj = storage.get(State, state_id)
    if obj is not None:
        obj = obj.to_dict()
    else:
        abort(404)

    return jsonify(obj)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_specific_state(state_id):
    """Deletes a state with specific id"""

    objs = storage.all(State).values()
    state = [obj.to_dict() for obj in objs if obj.id == state_id]
    if state is not None:
        print(f"STATE ==============> {state}")
        print(f"state[0] ===================> {state[0]}")
        state.remove(state[0])
        for obj in objs:
            if obj.id == state_id:
                storage.delete(obj)
                storage.save()
    else:
        abort(404)

    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def add_state():
    """Creates and adds a new state object"""

    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")

    new_obj = State(name=data['name'])
    storage.new(new_obj)
    storage.save()

    state = new_obj.to_dict()
    return jsonify(state), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a state object"""

    obj = storage.get(State, state_id)
    if obj is not None:
        data = request.get_json()
        if not data:
            abort(400, "Not a JSON")
        print(f"OBJECT =================> {obj}")
        obj.name = request.json['name']
        storage.save()
    else:
        abort(404)

    return jsonify(obj.to_dict()), 200
