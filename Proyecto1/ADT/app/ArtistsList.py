import os
import subprocess

from ADT.LinkedList import LinkedList
from models.Artist import Artist

class ArtistsList(LinkedList):

    def __init__(self):
        super().__init__()

    def printListAsc(self):
        currentValue: Artist = self.head

        while currentValue:
            print(currentValue.value)
            currentValue = currentValue.nextValue


    def findByID(self, aid):
        currentValue: Artist = self.head
        artistFound = None

        while currentValue is not None:
            if currentValue.value.aid == aid:
                artistFound = currentValue.value
                break
            currentValue = currentValue.nextValue

        return artistFound
    
    def draw(self):
        codedot = ''
        codedot += '''digraph G {
            rankdir=LR;
            node[shape=record, height=.1]
        '''
        counter_nodes = 1

        #CREAR LOS NODOS
        current = self.head
        while current:
            codedot += 'nodo'+str(counter_nodes)+'[label=\"{'+str(current.value)+'|<f1>}\"];\n'
            counter_nodes+=1
            current = current.nextValue
        
        #CREAR LOS ENLACES
        current = self.head
        counter_nodes = 1
        while current and current.nextValue:
            codedot += 'nodo'+str(counter_nodes)+' -> nodo'+str(counter_nodes+1)+';\n'
            counter_nodes+=1
            current = current.nextValue
        
        codedot += '}'

        #ESCRIBIR EL TEXTO CONCATENASO AL ARCHIVO DOT

        #defino la ruta donde se guarda el codigo dot
        dot_path = 'Proyecto1/dot_reports/simple_list.dot'
        #creamos el file_artist dot
        file_artist = open(dot_path,'w')
        #escribimos el archivo
        file_artist.write(codedot)
        #cerramos el file_artist
        file_artist.close()

        # GENERACIÓN DE LA IMAGEN
        
        #defino la ruta donde se guarda la imagen
        image_path = 'Proyecto1/reports/simple_list.png'
        #defino el command de graphviz para compilar el dot y generar la imagen
        command = 'dot -Tpng '+ dot_path + ' -o ' + image_path
        #ejecuto el command
        os.system(command)

        # ABRIR LA IMAGEN

        #1. CONVERTIMOS LA RUTA RELATIVA A UNA RUTA ABSOLUTA
        # RUTA RELATIVA: ./hola.txt
        # RUTA ABSOLUTA: C://users/equis/documents/hola.txt
        open_image_path = os.path.abspath(image_path)
        # os.startfile(open_image_path)
        subprocess.run(["open", open_image_path])
        print('Grafico generado con exito')