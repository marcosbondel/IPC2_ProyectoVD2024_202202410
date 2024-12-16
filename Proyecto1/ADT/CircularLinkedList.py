import os
import subprocess
from ADT.Node import SimpleNode

class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def append(self, value):
        newNode = SimpleNode(value)

        if self.head is None and self.last is None:
            self.head = newNode
            self.last = newNode
            self.size += 1
            return

        current = self.head

        while current.nextValue:
            current = current.nextValue

        current.nextValue = newNode
        newNode.nextValue = self.head
        self.last = newNode
        self.size += 1

    def showList(self):
        current = self.head

        while current and current != self.last:
            print(current)
            current = current.nextValue

    def draw(self):
        dot_code = ''

        #CREAMOS EL CODIGO PARA LA LISTA
        dot_code += '''digraph G {
            rankdir=LR;
            node[shape=record, height=.1]
        '''
        #CREAMOS LOS NODOS
        nodes_counter = 0
        current = self.head
        while nodes_counter < self.size:
            dot_code += 'nodo'+str(nodes_counter)+'[label=\"{'+str(current.valor)+'|<f1>}\"];\n'
            current = current.nextValue
            nodes_counter+=1
        
        #CREAMOS LOS ENLACES
        current = self.head
        nodes_counter = 0
        while nodes_counter < self.size-1:
            dot_code += 'nodo'+str(nodes_counter)+' -> nodo'+str(nodes_counter+1)+';\n'
            current = current.nextValue
            nodes_counter+=1
        
        #AGREGAMOS EL ULTIMO ENLACE
        dot_code += 'nodo'+str(self.size-1)+ ' -> nodo0[constraint=false];\n'

        dot_code += '}'

        #CREAMOS EL file DOT
        dot_path = 'Proyecto1/dot_reports/circular_list.dot'

        file = open(dot_path, 'w')
        file.write(dot_code)
        file.close()

        #GENERAR LA IMAGEN
        image_path = 'Proyecto1/reports/circular_list.png'
        

        command = 'dot -Tpng '+dot_path + ' -o '+image_path
        os.system(command)

        #ABRIMOS LA IMAGEN
        open_image_path = os.path.abspath(image_path)
        subprocess.run(["open", open_image_path])
