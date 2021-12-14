import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
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

@users.route('/register', methods=['POST']) 
def register():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()

    try:
        models.User.get(models.User.email == payload['email'])

        return jsonify(
            data={},
            message=f"A user with the email {payload['email']} already exists",
            status=401
        ), 401

    except models.DoesNotExist:
        pw_hash = generate_password_hash(payload['password'])

        create_user = models.User.create(
            username=payload['username'],
            email=payload['email'],
            zip=payload['zip'],
            password=pw_hash
        )

        login_user(create_user)

        created_user_dict = model_to_dict(create_user)
        created_user_dict.pop('password')

        return jsonify(
            data=created_user_dict,
            message=f"Successfully registered {created_user_dict['email']}",
            status=201
        ), 201