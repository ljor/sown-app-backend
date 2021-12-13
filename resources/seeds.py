import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

seeds = Blueprint('seeds', 'seeds')

# GET /api/v1/seeds
@seeds.route('/')
def seeds_index():
    result = models.Seed

    print('result of seed select query')
    print(result)

    return 'check your terminal'