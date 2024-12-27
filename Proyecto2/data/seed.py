import os
from xml.etree import ElementTree as ET
from models.user import User

users_list = []

def load():

    # - Load admin user -
    admin_ipc = User()

    admin_ipc.uid = 'AdminIPC'
    admin_ipc.full_name = 'AdminIPC'    
    admin_ipc.password = 'ARTIPC2'
    admin_ipc.email = ''    
    admin_ipc.phone = ''    
    admin_ipc.address = ''    
    admin_ipc.profile = ''    
    admin_ipc.role = 'admin'
    admin_ipc.figures = []

    users_list.append(admin_ipc)
    # users_list.append(User('AdminIPC', 'ARTIPC2', 'AdminIPC', 'AdminIPC', 'AdminIPC', 'AdminIPC', 'AdminIPC'))

    # - Load normal users -

    #Si no existe el archivo, retorna una lista vacia
    if not os.path.exists('Proyecto2/data/users.xml'):
        return []

    tree = ET.parse('Proyecto2/data/users.xml')
    root = tree.getroot()

    for user in root:
        new_user = User()
        new_user.uid = user.attrib['id']
        new_user.password = user.attrib['pwd']

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

        new_user.role = 'user'

        if new_user.is_valid():
            users_list.append(new_user)
    
    return users_list

def check_existance(id):

    for user in users_list:
        if user.uid == id:
            return True

    return False