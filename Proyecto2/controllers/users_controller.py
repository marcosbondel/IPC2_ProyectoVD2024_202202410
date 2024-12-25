from flask import Blueprint, jsonify, request
import os

from models.user import User
from utils.responder import respond_with_error

from xml.etree import ElementTree as ET


UserBlueprint = Blueprint('users', __name__)

@UserBlueprint.route('/users/load', methods=['POST'])
def users_load():
    try:
        xml_entry = request.data.decode('utf-8')

        users = []

        if xml_entry == '':
            return respond_with_error('Empty XML')

        root = ET.fromstring(xml_entry)

        for user in root:
            new_user = User()
            new_user.uid = user.attrib['uid']
            new_user.password = user.attrib['password']

            for attribute in user:
                match attribute:
                    case 'NombreCompleto':
                        new_user.full_name = attribute.text
                    case 'CorreoElectronico':
                        new_user.email = attribute.text
                    case 'NumeroTelefono':
                        new_user.phone = attribute.text
                    case 'Direccion':
                        new_user.address = attribute.text
                    case 'perfil':
                        new_user.profile = attribute.text

            if new_user.is_valid():
                users.append(new_user)



    except Exception as e:
        print(f'Something went wrong: {e}')

def create_xml(users_list):

    if os.path.exists('/data/users.xml'):
        os.remove('/data/users.xml')

    tree = ET.Element('users')

    for user in users_list:
        user: User
        user_xml = ET.SubElement(tree, 'user', id=user.uid, pwd=user.password)

        name = ET.SubElement(user_xml, 'NombreCompleto')
