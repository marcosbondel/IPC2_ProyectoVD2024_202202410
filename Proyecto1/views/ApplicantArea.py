import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.app.ApplicantsList import ApplicantsList
from ADT.app.ArtistsList import ArtistsList

class ApplicantArea:
    def __init__(self, parent, applicants_list: ApplicantsList, artists_list: ArtistsList):
        self.parent = parent
        self.admin_window = tk.Toplevel()
        self.admin_window.title("Área de Solicitante")
        self.admin_window.geometry("600x400")

        self.applicants_file_paths = ()
        self.artists_file_paths = ()
        self.applicants_list = applicants_list
        self.artists_list = artists_list

        # Welcome label
        welcome_label = tk.Label(self.admin_window, text="Bienvenido al Área de Solicitante", font=("Arial", 16))
        welcome_label.pack(pady=30)

        # Load applicatns button
        load_applicants_button = tk.Button(self.admin_window, text='Cargar solicitud', font=("Arial", 12), command=self.getApplicantsFilePaths)
        load_applicants_button.pack(pady=30)
        
        # # Load applicatns button
        # load_artists_button = tk.Button(self.admin_window, text='Cargar artistas', font=("Arial", 12), command=self.getArtistsFilePaths)
        # load_artists_button.pack(pady=40)

        # # Logout button
        # logout_button = tk.Button(self.admin_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        # logout_button.pack(pady=20)

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
            newApplicant.set_aid(applicant.attrib['id'])
            newApplicant.set_password(applicant.attrib['pwd'])

            for attr in applicant:
                match attr.tag:
                    case 'NombreCompleto':
                        newApplicant.set_full_name(attr.text)
                    case 'CorreoElectronico':
                        newApplicant.set_email(attr.text)
                    case 'NumeroTelefono':
                        newApplicant.set_phone(attr.text)
                    case 'Direccion':
                        newApplicant.set_address(attr.text)
            
            print(newApplicant.is_valid())
            if newApplicant.is_valid():
                self.applicants_list.append(newApplicant)
        
        self.applicants_list.printListAsc()
    
    def readArtistFile(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for artist in root:
            newArtist = Artist()
            newArtist.set_aid(artist.attrib['id'])
            newArtist.set_password(artist.attrib['pwd'])

            for attr in artist:
                match attr.tag:
                    case 'NombreCompleto':
                        newArtist.set_full_name(attr.text)
                    case 'CorreoElectronico':
                        newArtist.set_email(attr.text)
                    case 'NumeroTelefono':
                        newArtist.set_phone(attr.text)
                    case 'Especialidades':
                        newArtist.set_skills(attr.text)
                    case 'NotasAdicionales':
                        newArtist.set_notes(attr.text)
            
            if newArtist.is_valid():
                self.artists_list.append(newArtist)
        
        self.artists_list.printList()
