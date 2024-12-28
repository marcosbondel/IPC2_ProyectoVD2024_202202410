import os
from xml.etree import ElementTree as ET
from models.user import User
from models.Figure import Figure
from models.Pixel import Pixel

users_list = []
figures_list = []

def load_users():

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

        # Avoid duplicated admin user
        if user.attrib['id'] == 'AdminIPC':
            continue

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

    print('Users loaded successfully :)')
    
    return users_list

def load_figures():
    if not os.path.exists('Proyecto2/data/images.xml'):
        return []
    
    tree = ET.parse('Proyecto2/data/images.xml')
    root = tree.getroot()

    for figure in root:
        fid = int(figure.attrib['id'])
        uid = figure.attrib['id_usuario']
        edited = figure.attrib['editado']
        
        if edited == '1':
            edited = True
        elif edited == '0':
            edited = False
        
        new_figure = Figure()
        new_figure.fid = fid
        new_figure.uid = uid
        new_figure.edited = edited
        new_figure.design = []
        
        for attr in figure:
            match attr.tag:
                case 'nombre':
                    new_figure.name = attr.text
                case 'diseño':

                    for pixel in attr:
                        new_pixel = Pixel(
                            int(pixel.attrib['fila']),
                            int(pixel.attrib['col']),
                            pixel.text
                        )

                        new_figure.design.append(new_pixel)
        
        figures_list.append(new_figure)
    
    print('Images loaded successfully :)')
    
    return figures_list


def check_existance(id):

    for user in users_list:
        if user.uid == id:
            return True

    return False