from flask import Blueprint, request
from data.seed import users_list
from utils.responder import respond_with_success, respond_with_error

AuthBlueprint = Blueprint('auth', __name__)

@AuthBlueprint.route('/sign_in.json', methods=['POST'])
def sign_in():
    uid = request.json['id']
    password = request.json['password']

    for user in users_list:
        if user.uid == uid and user.password == password:
            return respond_with_success(user.to_dict())

    return respond_with_error('Datos incorrectos')
