import os
import subprocess
from ADT.Node import DoublyLinkedNode

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0

    def len(self):
        return self.length

    def append(self, value):
        newValue = DoublyLinkedNode(value)

        if self.head is None and self.last is None:
            self.head = newValue
            self.last = newValue
        else:
            currentValue = self.head

            while currentValue.nextValue:
                currentValue = currentValue.nextValue
                
            currentValue.nextValue = newValue
            newValue.previousValue = currentValue
            self.last = newValue

        self.length += 1

    def printListAsc(self):
        currentValue = self.head

        while currentValue is not None:
            print(currentValue)
            currentValue = currentValue.nextValue

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
        print('Se genero la grafica de la lista doblemente enlazada')