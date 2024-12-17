import os
import subprocess
from ADT.Node import SimpleNode

class Queue:

    def __init__(self):
        self.head = None
        self.size = 0

    def len(self):
        return self.size

    def enqueue(self, value):
        newNode:Node = SimpleNode(value)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        current = self.head

        while current:
            if current.nextValue is None:
                current.nextValue = newNode
                self.size += 1
                break
            current = current.nextValue


    def dequeue(self):

        if self.head is None:
            return None

        deleted = self.head.value

        self.head = self.head.nextValue
        self.size -= 1

        return deleted


    def first(self):
        return self.head

    def draw(self):
        dot_code = ''
        dot_code +='''digraph G {
            rankdir="RL";
            label="Cola";
            node[shape=box];
        '''
        counter = 0
        #creamos los nodos
        current = self.head
        while current != None:
            dot_code += 'nodo'+str(counter)+'[label=\"'+str(current.value)+'\"];\n'
            counter += 1
            current = current.nextValue

        #creamos los enlaces
        counter = 0
        current = self.head
        while current.nextValue != None:
            dot_code+='nodo'+str(counter)+' -> nodo'+str(counter+1)+';\n'
            counter+=1
            current = current.nextValue
        
        dot_code+='}'

        #crear nuestro file dot
        dot_pah = 'Proyecto1/dot_reports/queue.dot'

        file = open(dot_pah,'w')
        file.write(dot_code)
        file.close()

        #generamos la imagen
        image_path = 'Proyecto1/reports/queue.png'

        command = 'dot -Tpng '+dot_pah+' -o '+image_path
        os.system(command)

        #abrimos la imagen
        open_image_path = os.path.abspath(image_path)
        subprocess.run(["open", open_image_path])
        