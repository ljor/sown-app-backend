import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

seeds = Blueprint('seeds', 'seeds')

# seed index route
@seeds.route('/')
def seeds_index():
    result = models.Seed

    seed_dicts = [model_to_dict(seed) for seed in result]

    return jsonify({
        'data': seed_dicts,
        'message': f"Successfully found {len(seed_dicts)} seeds",
        'status': 200
    }), 200

# seed create route
@seeds.route('/', methods=['POST'])
def create_seed():
    payload = request.get_json()
    print(payload)

    new_seed = models.Seed.create(name=payload['name'], category=payload['category'], indoor_sow_start=payload['indoor_sow_start'], indoor_sow_end=payload['indoor_sow_end'], direct_sow_start=payload['direct_sow_start'], direct_sow_end=payload['direct_sow_end'], img=payload['img'], maturity=payload['maturity'], description=payload['description'])
    print(new_seed)

    seed_dict = model_to_dict(new_seed)

    return jsonify(
        data=seed_dict,
        message='Successfully created seed',
        status=201
    ), 201

# seed show route
@seeds.route('/<id>', methods=['GET'])
def get_one_seed(id):
    seed = models.Seed.get_by_id(id)
    print(seed)
    return jsonify(
        data = model_to_dict(seed),
        message = 'Successfully retrieved seed',
        status = 200
    ), 200

@seeds.route('/<id>', methods=['PUT'])
def update_seed(id):
    payload = request.get_json()

    models.Seed.update(**payload).where(models.Seed.id == id).execute()

    return jsonify(
        data = model_to_dict(models.Seed.get_by_id(id)),
        message = 'seed updated successfully',
        status = 200,
    ), 200