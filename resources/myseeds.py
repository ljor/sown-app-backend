from playhouse.shortcuts import model_to_dict
import models

from flask import Blueprint, jsonify
from flask_login.utils import login_required
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

myseeds = Blueprint('myseeds', 'myseeds')

# get route for my seeds
@myseeds.route('/')
@login_required
def myseeds_index():
    result = models.UserSeed.select()

    current_user_seed_dicts = [model_to_dict(seed) for seed in current_user.myseeds]

    return jsonify({
        'data': current_user_seed_dicts,
        'message': f"Succsessfully found {len(current_user_seed_dicts)} seeds",
        'status': 200
    }), 200