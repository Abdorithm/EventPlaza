#!/usr/bin/env python3
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from flasgger import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_users():
    """
    Get all users
    """
    all_users = storage.all("User").values()
    list_users = [user.to_dict() for user in all_users]
    return jsonify(list_users)

@app_views.route('/users/<id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml')
def get_user(id):
    """
    Get a user given his id
    """
    print(id, type(id))
    user = storage.get("User", id);

    if user is None:
        abort(404)
    return jsonify(user.to_dict())
