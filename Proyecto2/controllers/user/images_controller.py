import os
from xml.etree import ElementTree as ET

# from controllers.usuarioController import preCargarXML
from data.seed import figures_list
from flask import Blueprint, jsonify, request
from models.SparseMatrix.MatrizDispersa import MatrizDispersa
from models.Pixel import Pixel
from models.Figure import Figure

from utils.responder import respond_with_error, respond_with_success

ImageBlueprint = Blueprint('images', __name__)

@ImageBlueprint.route('/user/<string:uid>/images.json', methods=['POST'])
def load_images(uid):
    
    try:
        xml_entry = request.data.decode('utf-8')

        if xml_entry == '':
            return respond_with_error('No se recibió el archivo XML')

        root = ET.fromstring(xml_entry)
        
        matrix = MatrizDispersa()
        
        new_figure = Figure()
        new_figure.fid = len(figures_list) + 1
        new_figure.uid = uid
        new_figure.edited = False
        new_figure.design = []

        for attr in root:
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

                        matrix.insertar(
                            int(pixel.attrib['fila']),
                            int(pixel.attrib['col']),
                            pixel.text
                        )

                        new_figure.design.append(new_pixel)

        
        figures_list.append(new_figure)
        crearXML(figures_list)

        return respond_with_success({
            'matrix': matrix.graficar()
        })
    
    except Exception as e:
        print(f'ERROR: {e}')
        return respond_with_error('Error al cargar la imagen')

    
@ImageBlueprint.route('/user/<string:uid>/images/edit', methods=['POST'])
def editarImagen(uid):
    '''
    JSON DE ENTRADA
    {
        'id': id de la imagen,
        'filtro': 1 para escala de grises/2 para tonalidad sepia
    }
    '''

    id = int(request.json['id'])
    filtro = int(request.json['filtro'])
    current_image = None

    for figure in figures_list:
        if figure.uid == id:
            current_image = figure
            break

    if current_image is None:
        return respond_with_error('Imagen no encontrada')
    
    #1. Creamos una lista de nuevos pixeles para crear la nueva imagen
    nuevos_pixeles = []
    #Matriz1: Matriz original
    matriz1 = MatrizDispersa()
    #Matriz2: Matriz Editada
    matriz2 = MatrizDispersa()

    #Recorro la imagen original para insertarlo a la matriz dispersa 1
    for pixel in current_image.design:
        #Insertamos los pixeles a la matriz1
        matriz1.insertar(pixel.row, pixel.col, pixel.data)

        #Aplicamos filtros
        #1. Escala de grises
        if filtro == 1:
            #1. Pasamos de hexadecimal a RGB
            rgb_pixel = HexToRGB(pixel.data)
            #2. Pasamos el RGB a escala de grises
            rgb_escala_grises = rgbToGrayScale(rgb_pixel)
            #3. Pasamos el escala de grises a hexadecimal
            nuevo_color = rgbToHex(rgb_escala_grises)
            #4. Insertamos el nuevo pixel a la matriz2
            matriz2.insertar(pixel.row, pixel.col, nuevo_color)
            #5. Creamos un nuevo pixel
            nuevo_pixel = Pixel(pixel.row, pixel.col, nuevo_color)
            nuevos_pixeles.append(nuevo_pixel)
        #2. Tonalidad sepia
        elif filtro == 2:
            #1. Pasamos de hexadecimal a RGB
            rgb_pixel = HexToRGB(pixel.color)
            #2. Pasamos el RGB a sepia
            rgb_sepia = rgbToSepia(rgb_pixel)
            #3. Pasamos la tonalidad sepia a hexadecimal
            nuevo_color = rgbToHex(rgb_sepia)
            #4. Insertamos el nuevo pixel a la matriz2
            matriz2.insertar(pixel.fila, pixel.columna, nuevo_color)
            #5. Creamos un nuevo pixel
            nuevo_pixel = Pixel(pixel.fila, pixel.columna, nuevo_color)
            nuevos_pixeles.append(nuevo_pixel)
    
    #2. Creamos una nueva imagen con los pixeles nuevos
    new_figure = Figure(id, current_image.name, uid,)

    new_figure = Figure()
    new_figure.fid = len(figures_list) + 1
    new_figure.name = current_image.name
    new_figure.uid = uid
    new_figure.design = nuevos_pixeles
    new_figure.edited = True

    figures_list.append(new_figure)
    crearXML(figures_list)

    return respond_with_success({
        'mensaje': 'Imagen editada correctamente',
        'matriz1': matriz1.graficar(),
        'matriz2': matriz2.graficar(),
    })

def HexToRGB(hex_color):
    """
    Convierte un color en formato hexadecimal (#RRGGBB) a formato RGB.

    Args:
        hex_color (str): Color en formato hexadecimal (por ejemplo, '#FFFFFF').

    Returns:
        tuple: Una tupla con los valores RGB (rojo, verde, azul).
    """

    #Eliminamos el simbolo '#'
    hex_color = hex_color.lstrip('#')

    #convertimos el string hexadecimal a valores RGB
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return (red, green, blue)

def rgbToGrayScale(rgb_color):
    """
    Convierte un color RGB a su equivalente en escala de grises (en formato RGB).

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        tuple: Una tupla con los valores RGB en escala de grises.
    """

    red, green, blue = rgb_color

    #Obtenemos el nuevo gris
    gris = 0.2989*red + 0.5870*green + 0.1140*blue

    gris = round(gris)

    return (gris, gris, gris)

def rgbToSepia(rgb_color):
    """
    Convierte un color RGB a su equivalente en tonalidad sepia (en formato RGB).

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        tuple: Una tupla con los valores RGB en tonalidad sepia.
    """

    red,green, blue = rgb_color

    #calculamos los nuevos colores
    new_red = 0.393*red + 0.769*green + 0.189*blue
    new_green = 0.349*red + 0.686*green + 0.168*blue
    new_blue = 0.272*red + 0.534*green + 0.131*blue

    new_red = round(new_red)
    new_green = round(new_green)
    new_blue = round(new_blue)

    return (new_red, new_green, new_blue)

def rgbToHex(rgb_color):
    """
    Convierte un color en formato RGB a un string en formato hexadecimal.

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        str: El color en formato hexadecimal (por ejemplo, '#RRGGBB').
    """

    return "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def crearXML(imagenes):
    #si existe el archivo, se elimina
    if os.path.exists('Proyecto2/data/images.xml'):
        os.remove('Proyecto2/data/images.xml')
    
    #CREAR EL XML
    tree = ET.Element('imagenes')
    for imagen in imagenes:
        editado = 0
        if imagen.edited == True:
            editado = 1
        imagen_xml = ET.SubElement(tree, 'imagen', id=str(imagen.fid), id_usuario=str(imagen.uid), editado=str(editado))
        nombre_xml = ET.SubElement(imagen_xml, 'nombre')
        nombre_xml.text = imagen.name
        diseño_xml = ET.SubElement(imagen_xml, 'diseño')
        for pixel in imagen.design:
            pixel_xml = ET.SubElement(diseño_xml, 'pixel', fila=str(pixel.row), col=str(pixel.col))
            pixel_xml.text = pixel.data
    
    tree = ET.ElementTree(tree)

    ET.indent(tree, space='\t', level=0)

    tree.write('Proyecto2/data/images.xml', encoding='utf-8', xml_declaration=True)
