import os
import subprocess
from ADT.DoublyLinkedList import DoublyLinkedList
from models.Applicant import Applicant

class ApplicantsList(DoublyLinkedList):

    def __init__(self):
        super().__init__()

    def printListAsc(self):
        currentValue: Applicant = self.head

        while currentValue is not None:
            print(currentValue.value)
            currentValue = currentValue.nextValue

    def findByID(self, id):
        currentValue: Applicant = self.head
        applicantFound = None

        while currentValue is not None:
            if currentValue.value.aid == id:
                applicantFound = currentValue.value
                break
            currentValue = currentValue.nextValue

        return applicantFound

    def draw(self):
        dot_code = ''
        dot_code += '''digraph G {
            rankdir=LR;
            node[shape=record, height=.1]
        '''
        
        #CREAMOS LOS NODOS
        current = self.head
        counter_nodes = 1

        while current:
            dot_code += 'nodo'+str(counter_nodes)+'[label=\"{<f1>|'+str(current.value)+'|<f2>}\"];\n'
            counter_nodes+=1
            current = current.nextValue
        
        #CREAMOS LOS ENLACES
        current = self.head
        counter_nodes = 1
        while current and current.nextValue:
            #RELACION DE IZQUIERDA A DERECHA
            dot_code += 'nodo'+str(counter_nodes)+':f2 -> nodo'+str(counter_nodes+1)+':f1;\n'
            #RELACION DE DERECHA A IZQUIERDA
            dot_code += 'nodo'+str(counter_nodes+1)+':f1 -> nodo'+str(counter_nodes)+':f2;\n'
            counter_nodes+=1
            current = current.nextValue
        
        dot_code += '}'

        #CREAMOS Y ESCRIBIMOS EL applicant_file .DOT
        dot_path = 'Proyecto1/dot_reports/doubly_linked_list.dot'


        #creo el applicant_file
        applicant_file = open(dot_path, 'w')
        applicant_file.write(dot_code)
        applicant_file.close()

        #generamos la imagen
        img_path = 'Proyecto1/reports/doubly_linked_list.png'
        command = 'dot -Tpng ' + dot_path + ' -o ' + img_path
        os.system(command)

        #CONVIERTO LA RUTA RELATIVA A RUTA ABSOLUTA
        open_image_path = os.path.abspath(img_path)
        # os.startfile(open_image_path)
        subprocess.run(["open", open_image_path])