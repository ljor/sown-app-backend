import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

seeds = Blueprint('seeds', 'seeds')

# seed index route
@seeds.route('/')
def seeds_index():
    result = models.Seed

    print('result of seed select query')
    print(result)

    return 'check your terminal'

# seed create route
@seeds.route('/', methods=['POST'])
def create_seed():
    payload = request.get_json()
    print(payload)

    return 'you hit the create route'