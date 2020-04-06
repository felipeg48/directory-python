from flask import Flask, jsonify, make_response, request, abort
from person_repository import add_person, find_person_by_email, get_all_persons, update_person, remove_person
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found or Cannot Complete action'}), 404)


@app.route('/', methods=['GET'])
def get_all():
    return jsonify(get_all_persons())


@app.route('/persons', methods=['POST'])
def new_person():
    return jsonify(add_person(request.json)), 201


@app.route('/persons/<email>', methods=['GET'])
def get_person(email):
    person = find_person_by_email(email)
    if person is None:
        abort(404)
    return jsonify(person), 200


@app.route('/persons', methods=['PUT'])
def update():
    person = update_person(request.json)
    if person is None:
        abort(404)
    return jsonify(person),202

@app.route('/persons/<email>', methods=['DELETE'])
def delete_person(email):
    person = remove_person(email)
    if person is None:
        abort(404)
    return jsonify(person), 200