import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

# user get route for testing
@users.route('/')
def user_test_route():
    result = models.User
    
    user_dicts = [model_to_dict(user) for user in result]

    return jsonify({
        'data': user_dicts,
        'message': f"Successfully found {len(user_dicts)} users",
        'status': 200
    }), 200 