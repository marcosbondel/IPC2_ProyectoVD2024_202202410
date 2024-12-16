import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.Pile import Pile
from ADT.DoublyLinkedList import DoublyLinkedList
from ADT.CircularLinkedList import CircularLinkedList
from ADT.app.ApplicantsList import ApplicantsList
from ADT.app.ArtistsList import ArtistsList
from models.Applicant import Applicant
from models.Artist import Artist

class AdminArea:
    def __init__(self, parent, applicants_list: ApplicantsList, artists_list: ArtistsList):
        self.parent = parent
        self.admin_window = tk.Toplevel()
        self.admin_window.title("Área de Administración")
        self.admin_window.geometry("900x700")

        self.applicants_file_paths = None
        self.artists_file_paths = None
        self.applicants_list = applicants_list
        self.artists_list = artists_list

        # Welcome label
        welcome_label = tk.Label(self.admin_window, text="Bienvenido al Área de Administración", font=("Arial", 16))
        welcome_label.pack(pady=30)

        # Load applicants button
        load_applicants_button = tk.Button(self.admin_window, text='Cargar solicitantes', font=("Arial", 12), command=self.getApplicantsFilePaths)
        load_applicants_button.pack(pady=30)
        
        # Load artists button
        load_artists_button = tk.Button(self.admin_window, text='Cargar artistas', font=("Arial", 12), command=self.getArtistsFilePaths)
        load_artists_button.pack(pady=35)
        
        # View applicants button
        view_applicants_button = tk.Button(self.admin_window, text='Ver solicitantes', font=("Arial", 12), command=self.applicants_list.draw)
        view_applicants_button.pack(pady=40)

        # View applicants button
        view_artists_button = tk.Button(self.admin_window, text='Ver artistas', font=("Arial", 12), command=self.artists_list.draw)
        view_artists_button.pack(pady=45)

        # Logout button
        logout_button = tk.Button(self.admin_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        """Logout and return to the login window."""
        self.admin_window.destroy()
        self.parent.deiconify()

    def getApplicantsFilePaths(self):
        self.applicants_file_paths = XMLHandler().getFilePaths()

        for file_path in self.applicants_file_paths:
            self.readApplicantFile(file_path)

    def getArtistsFilePaths(self):
        self.artists_file_paths = XMLHandler().getFilePaths()

        for file_path in self.artists_file_paths:
            self.readArtistFile(file_path)

    def readApplicantFile(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for applicant in root:
            newApplicant = Applicant()
            newApplicant.aid = applicant.attrib['id']
            newApplicant.password = applicant.attrib['pwd']

            for attr in applicant:
                match attr.tag:
                    case 'NombreCompleto':
                        newApplicant.full_name = attr.text
                    case 'CorreoElectronico':
                        newApplicant.email = attr.text
                    case 'NumeroTelefono':
                        newApplicant.phone = attr.text
                    case 'Direccion':
                        newApplicant.address = attr.text

            if newApplicant.is_valid():
                newApplicant.pile = Pile()    
                newApplicant.accepted_figures = DoublyLinkedList()
                self.applicants_list.append(newApplicant)

    def readArtistFile(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for artist in root:
            newArtist = Artist()
            newArtist.aid = artist.attrib['id']
            newArtist.password = artist.attrib['pwd']

            for attr in artist:
                match attr.tag:
                    case 'NombreCompleto':
                        newArtist.full_name = attr.text
                    case 'CorreoElectronico':
                        newArtist.email = attr.text
                    case 'NumeroTelefono':
                        newArtist.phone = attr.text
                    case 'Especialidades':
                        newArtist.skills = attr.text
                    case 'NotasAdicionales':
                        newArtist.notes = attr.text
            
            if newArtist.is_valid():
                newArtist.accepted_figures = DoublyLinkedList()
                self.artists_list.append(newArtist)
