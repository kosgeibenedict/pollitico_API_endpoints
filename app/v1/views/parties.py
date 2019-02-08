from flask import make_response, jsonify, request, Blueprint
from app.v1.models.parties import PoliticalParty, parties

api = Blueprint('parties', __name__,  url_prefix='/api/v1/')

@api.route('/parties', methods=["POST"])
def create_party():
    data = request.get_json(force=True)
    if len(parties) == 0:
        _id = 1
    else:
        _id = parties[-1]['id'] + 1

    #if data['name'] == '' or data['address'] == '' or data['logo'] == '':
    if data.get('name','') == '' or data.get('address','')=='' or data.get('logo','')=='':
        return make_response(jsonify({
            "status":400,
            "error": 'All fields are required'
        }), 400)
    
    new_party = {
        "id":_id,
        "name": data['name'],
        "hqAddress": data['address'],
        "logoUrl": data['logo']
    }

    res = PoliticalParty().save_party(new_party)


    return make_response(jsonify({
        "status":201,
        "data": [res]
    }), 201)