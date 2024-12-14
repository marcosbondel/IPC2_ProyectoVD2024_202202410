import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.Queue import Queue
from models.Artist import Artist

class ArtistArea:
    def __init__(self, parent, artist: Artist, figures_requested_queue):
        self.parent = parent
        self.admin_window = tk.Toplevel()
        self.admin_window.title("Área de Artista")
        self.admin_window.geometry("600x400")

        self.artist_session = artist
        self.figures_requested_queue: Queue = figures_requested_queue

        # Welcome label
        welcome_label = tk.Label(self.admin_window, text="Bienvenido al Área de Artista", font=("Arial", 16))
        welcome_label.pack(pady=30)

        # Accept button
        accept_button = tk.Button(self.admin_window, text='Aceptar', font=("Arial", 12), command=self.figures_requested_queue.draw)
        accept_button.pack(pady=40)
        
        # View queue button
        view_queue_button = tk.Button(self.admin_window, text='Ver cola', font=("Arial", 12), command=self.figures_requested_queue.draw)
        view_queue_button.pack(pady=50)
        
        # Accepted pictures button
        accepted_pictures_button = tk.Button(self.admin_window, text='Imagenes solicitadas', font=("Arial", 12), command=self.figures_requested_queue.draw)
        accepted_pictures_button.pack(pady=60)
        

        # Logout button
        logout_button = tk.Button(self.admin_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        """Logout and return to the login window."""
        self.admin_window.destroy()
        self.parent.deiconify()


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
        
        # self.applicants_list.printListAsc()
    
