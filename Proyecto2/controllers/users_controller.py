from flask import Blueprint, request
from xml.etree import ElementTree as ET
import os

from models.user import User
from utils.responder import respond_with_success, respond_with_error
from data.seed import users_list, check_existance


UserBlueprint = Blueprint('users', __name__)

@UserBlueprint.route('/users/load.json', methods=['POST'])
def users_load():
    try:
        xml_entry = request.data.decode('utf-8')

        if xml_entry == '':
            return respond_with_error('Empty XML')

        root = ET.fromstring(xml_entry)

        for user in root:
            new_user = User()
            new_user.uid = user.attrib['id']
            new_user.password = user.attrib['pwd']
            new_user.role = 'user'
            new_user.figures = []
            
            # Check user existance
            if check_existance(new_user.uid):
                continue

            for attribute in user:
                match attribute.tag:
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
                users_list.append(new_user)
        
        create_xml(users_list)

        return respond_with_success('Users loaded successfully :)')
    except Exception as e:
        print(f'Something went wrong: {e}')
        return respond_with_error(e)


@UserBlueprint.route('/users.json', methods=['GET'])
def index_users_json():
    return respond_with_success([user.to_dict() for user in users_list if user.uid != 'AdminIPC'])


@UserBlueprint.route('/users.xml', methods=['GET'])
def index_users_xml():
    tree = ET.Element('users')

    for user in users_list:
        usuario_xml = ET.SubElement(tree, 'user', id=user.uid, pwd=user.password)

        full_name = ET.SubElement(usuario_xml, 'NombreCompleto')
        full_name.text = user.full_name

        email = ET.SubElement(usuario_xml, 'CorreoElectronico')
        email.text = user.email

        phone = ET.SubElement(usuario_xml, 'NumeroTelefono')
        phone.text = user.phone

        address = ET.SubElement(usuario_xml, 'Direccion')
        address.text = user.address

        profile = ET.SubElement(usuario_xml, 'perfil')
        profile.text = user.profile

        imagenes = ET.SubElement(usuario_xml, 'figures')
    
    ET.indent(tree, space='\t', level=0)
    xml_str = ET.tostring(tree, encoding='utf-8', xml_declaration=True)

    return xml_str

def create_xml(users_list):

    if os.path.exists('Proyecto2/data/users.xml'):
        os.remove('Proyecto2/data/users.xml')

    tree = ET.Element('solicitantes')

    for user in users_list:
        user: User
        user_xml = ET.SubElement(tree, 'solicitante', id=user.uid, pwd=user.password)

        full_name = ET.SubElement(user_xml, 'NombreCompleto')
        full_name.text = user.full_name
        
        email = ET.SubElement(user_xml, 'CorreoElectronico')
        email.text = user.email
        
        phone = ET.SubElement(user_xml, 'NumeroTelefono')
        phone.text = user.phone
        
        address = ET.SubElement(user_xml, 'Direccion')
        address.text = user.address
        
        profile = ET.SubElement(user_xml, 'perfil')
        profile.text = user.profile

    
    tree = ET.ElementTree(tree)
    ET.indent(tree, space='\t', level=0)
    tree.write('Proyecto2/data/users.xml', encoding='utf-8', xml_declaration=True)