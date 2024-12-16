import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.LinkedList import LinkedList
from ADT.Pile import Pile
from ADT.Queue import Queue
from ADT.Node import SimpleNode
from ADT.app.ApplicantsList import ApplicantsList
from ADT.app.ArtistsList import ArtistsList
from models.Applicant import Applicant
from models.BFigure import BFigure
from models.BPixel import BPixel

class ApplicantArea:
    def __init__(self, parent, requested_pictures_queue: Queue, applicant: Applicant, applicants_list: ApplicantsList, artists_list: ArtistsList):
        self.parent = parent
        self.applicant_window = tk.Toplevel()
        self.applicant_window.title("Área de Solicitante")
        self.applicant_window.geometry("500x700")

        self.figures_file_paths = None
        self.imported_figures = 0

        self.applicant_session = applicant
        self.requested_pictures_queue = requested_pictures_queue

        # Welcome label
        welcome_label = tk.Label(self.applicant_window, text=f'Bienvenid@ al Área de Solicitante\n{self.applicant_session.full_name}', font=("Arial", 16))
        welcome_label.pack(pady=30)

        # Load applicatns button
        load_figures_button = tk.Button(self.applicant_window, text='Cargar solicitud', font=("Arial", 12), command=self.getPicturesFilePaths)
        load_figures_button.pack(pady=30)
        
        # Request button
        request_button = tk.Button(self.applicant_window, text='Solicitar', font=("Arial", 12), command=self.request_figure)
        request_button.pack(pady=40)
        
        # View pile button
        view_pile_button = tk.Button(self.applicant_window, text='Ver Pila', font=("Arial", 12), command=self.view_pile_report)
        view_pile_button.pack(pady=50)
       
        # View pile button
        view_list_button = tk.Button(self.applicant_window, text='Ver Lista', font=("Arial", 12), command=self.view_list_report)
        view_list_button.pack(pady=60)

        # Logout button
        logout_button = tk.Button(self.applicant_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        self.applicant_window.destroy()
        self.parent.deiconify()

    def view_pile_report(self):
        if self.applicant_session.pile.len() == 0:
            messagebox.showinfo("Ohoh", "La pila esta vacia...")
            return

        self.applicant_session.pile.draw()

    def view_list_report(self):
        if self.applicant_session.accepted_figures.len() == 0:
            messagebox.showinfo("Ohoh", "La lista esta vacia...")
            return

        self.applicant_session.accepted_figures.draw()


    def getPicturesFilePaths(self):
        self.figures_file_paths = XMLHandler().getFilePaths()

        self.imported_figures = 0

        for file_path in self.figures_file_paths:
            self.readFiguresFiles(file_path)

        if self.imported_figures == 0:
            messagebox.showinfo("Ohhh", 'Ninguna figura fue cargada :"(')

        messagebox.showinfo("Yeahh", "Figura(s) cargadas correctamente :)")

    def readFiguresFiles(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        newFigure = BFigure()
        newFigure.artist = None

        for child in root:
            match child.tag:
                case 'nombre':
                    newFigure.bId = child.attrib['id']
                    newFigure.name = child.text
                case 'diseño':
                    for pixel in child:
                        newPixel = BPixel(
                            pixel.attrib['fila'], 
                            pixel.attrib['col'], 
                            pixel.text
                        )

                        newFigure.design = LinkedList()
                        newFigure.design.append(newPixel)
                    

        newFigure.applicant = self.applicant_session
        self.applicant_session.pile.push(newFigure)
        self.imported_figures += 1

    def request_figure(self):

        peek = self.applicant_session.pile.pop()

        if not peek:
            messagebox.showinfo("Ohhhhh", "La pila esta vacia -_-")
            return

        self.requested_pictures_queue.enqueue(peek.value)
        print(f'Peek value: {peek.value}')

        messagebox.showinfo("Informacion", "Solicitud enviada a la cola :)")