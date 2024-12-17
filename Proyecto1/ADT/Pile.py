import os
import subprocess
from ADT.Node import NodePile

class Pile:

    def __init__(self):
        self.peek = None
        self.size = 0

    def len(self):
        return self.size

    def push(self, value):
        newNode = NodePile(value)

        newNode.down = self.peek
        self.peek = newNode

        self.size += 1

    def pop(self):

        if self.peek is None: 
            return None

        node_to_delete = self.peek

        self.peek = self.peek.down

        self.size -= 1

        return node_to_delete

    def peek(self):
        return self.peek

    def draw(self, aid = ''):
        dot_code = ''
        dot_code += '''digraph G {
            rankdir=LR;
            node[shape=Mrecord];
        '''

        print(f'Peek: {self.peek}')

        #CREAMOS EL NODO DE LA PILA
        dot_code += 'Pila[xlabel=\"Pila\" label=\"'
        #GRAFICAMOS LOS NODOS DE LA PILA
        current = self.peek
        while current != None:
            if current.down != None:
                dot_code+=str(current.value) + '|'
            else:
                dot_code+=str(current.value)
            current = current.down
        dot_code+='\"];\n'
        dot_code+='}'

        #CREAMOS EL file_pile DOT
        path_dot = f'Proyecto1/dot_reports/pile_{aid}.dot'
        file_pile = open(path_dot,'w')
        file_pile.write(dot_code)
        file_pile.close()

        #GENERAMOS LA IMAGEN
        image_path = f'Proyecto1/reports/pile_{aid}.png'
        comando = 'dot -Tpng '+path_dot+ ' -o '+image_path
        os.system(comando)

        #ABRIR LA IMAGEN
        open_image_path = os.path.abspath(image_path)
        subprocess.run(["open", open_image_path])
        print('Grafico de pila generado con exito :)')
        