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

# user register route
@users.route('/register', methods=['POST']) 
def register():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()

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

# user login route
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()

    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
        password_is_good = check_password_hash(user_dict['password'], payload['password'])

        if (password_is_good):
            login_user(user)
            print(f"Welcome, {current_user.username}")
            
            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message=f"Successfully logged in as {user_dict['username']}",
                status=200
            ), 200

        else:
            return jsonify(
                data={},
                message="Email or password is incorrect",
                status=401
            ), 401

    except models.DoesNotExist:
        print('not found')
        return jsonify(
            data={},
            message='Email not found',
            status=401
        ), 401

# user logout route
@users.route('/logout')
def logout():
    logout_user()
    return jsonify(
        data={},
        message='Successfully logged out',
        status=200
    ), 200

# check current user test route
@users.route('/user', methods=['GET'])
def get_logged_in_user():

    if not current_user.is_authenticated:
        return jsonify(
            data={},
            message="No user is currently logged in",
            status=401
        ), 401
    else:
        print(f"{current_user.username} is current_user.name in GET logged_in_user")
        user_dict = model_to_dict(current_user)
        user_dict.pop('password')

        return jsonify(
            data=user_dict,
            message=f"Currently logged in as {user_dict['email']}",
            status=200
        ), 200