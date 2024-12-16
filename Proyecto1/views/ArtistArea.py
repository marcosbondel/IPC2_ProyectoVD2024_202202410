import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.Queue import Queue
from models.Artist import Artist

class ArtistArea:
    def __init__(self, parent, artist: Artist, requested_figures_queue):
        self.parent = parent
        self.admin_window = tk.Toplevel()
        self.admin_window.title("Área de Artista")
        self.admin_window.geometry("400x600")

        self.artist_session = artist
        self.requested_figures_queue: Queue = requested_figures_queue

        # Welcome label
        welcome_label = tk.Label(self.admin_window, text="Bienvenido al Área de Artista", font=("Arial", 16))
        welcome_label.pack(pady=30)
       
       
        # Queue label
        print(f'Queue first value: {self.requested_figures_queue.first().value.showInfoInArtistArea()}')
        queue_label = tk.Label(self.admin_window, text=f"FIGURA SOLICITADA\n{self.requested_figures_queue.first().value.showInfoInArtistArea()}", font=("Arial", 16))
        queue_label.place(x=200,y=100)

        # Accept button
        accept_button = tk.Button(self.admin_window, text='Aceptar', font=("Arial", 12), command=self.acceptFigure)
        accept_button.place(x=50,y=100)
        
        # View queue button
        view_queue_button = tk.Button(self.admin_window, text='Ver cola', font=("Arial", 12), command=self.view_queue_report)
        view_queue_button.place(x=50,y=200)
        
        # Accepted pictures button
        accepted_pictures_button = tk.Button(self.admin_window, text='Imagenes solicitadas', font=("Arial", 12), command=self.view_accepted_figures_report)
        accepted_pictures_button.place(x=50,y=300)

        # Logout button
        logout_button = tk.Button(self.admin_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        # logout_button.pack(pady=60)
        logout_button.place(x=50,y=400)

    def logout(self):
        """Logout and return to the login window."""
        self.admin_window.destroy()
        self.parent.deiconify()


    def getArtistsFilePaths(self):
        self.artists_file_paths = XMLHandler().getFilePaths()

        for file_path in self.artists_file_paths:
            self.readArtistFile(file_path)

    def acceptFigure(self):

        if self.requested_figures_queue.len() == 0:
            messagebox.showwarning("Informacion", "No existen solicitudes de figuras -_-")
            return

        accepted_figure = self.requested_figures_queue.dequeue()
        accepted_figure.applicant.accepted_figures.append(accepted_figure)
        self.artist_session.accepted_figures.append(accepted_figure)

        messagebox.showinfo("Solicitud", f"Figura '{accepted_figure.name}' aceptada correctamente :)")

    def view_queue_report(self):
        if self.requested_figures_queue.len() == 0:
            messagebox.showinfo("Ohoh", "La cola esta vacia...")
            return

        self.requested_figures_queue.draw()

    def view_accepted_figures_report(self):
        if self.artist_session.accepted_figures.len() == 0:
            messagebox.showinfo("Ohoh", "La lista esta vacia...")
            return

        self.artist_session.accepted_figures.draw()

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
            
            if newApplicant.is_valid():
                self.applicants_list.append(newApplicant)