import tkinter as tk
from tkinter import messagebox
from views.AdminArea import AdminArea
from views.ApplicantArea import ApplicantArea
from views.ArtistArea import ArtistArea

from ADT.app.ApplicantsList import ApplicantsList
from ADT.app.ArtistsList import ArtistsList
from ADT.Queue import Queue

class LoginApp:
    def __init__(self, root, requested_figures_queue: Queue, applicants_list: ApplicantsList, artists_list: ArtistsList):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.create_login_ui()

        self.requested_figures_queue = requested_figures_queue
        self.applicants_list = applicants_list
        self.artists_list = artists_list

    def create_login_ui(self):
        """Create the login interface."""
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        # Title label
        title_label = tk.Label(frame, text="Sistema de Login", font=("Arial", 18))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username field
        username_label = tk.Label(frame, text="Usuario:", font=("Arial", 12))
        username_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.username_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.username_entry.grid(row=1, column=1, pady=10, padx=10)

        # Password field
        password_label = tk.Label(frame, text="Contraseña:", font=("Arial", 12))
        password_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
        self.password_entry.grid(row=2, column=1, pady=10, padx=10)

        # Login button
        login_button = tk.Button(frame, text="Iniciar sesión", font=("Arial", 12), width=15, command=self.handle_login)
        login_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Exit button
        exit_button = tk.Button(frame, text="Salir", font=("Arial", 12), width=15, command=self.root.quit)
        exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def handle_login(self):
        """Handle the login logic."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username.startswith('IPC-'):
            applicant_found = self.applicants_list.findByID(username)

            if not applicant_found:
                messagebox.showerror("Login", "Solicitante no existe")
                return

            if applicant_found.password == password:
                self.open_applicant_area(applicant_found)
                return
                
            messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")
        elif username.startswith('ART-'):
            artist_found = self.artists_list.findByID(username)

            if not artist_found:
                messagebox.showerror("Login", "Artista no existe")
                return

            if artist_found.password == password:
                self.open_artist_area(artist_found)
                return
            

            messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")
        # if username == "AdminIPC" and password == "ARTIPC2":
        elif username == "AdminIPC" and password == "ARTIPC2":
        # elif username == "test" and password == "test":
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            self.open_admin_area()
        else:
            messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")

    def open_admin_area(self):
        """Open the admin area."""
        self.root.withdraw()  # Hide the login window
        AdminArea(self.root, self.applicants_list, self.artists_list)
    
    def open_applicant_area(self, applicant_found):
        """Open the admin area."""
        self.root.withdraw()  # Hide the login window
        ApplicantArea(self.root, self.requested_figures_queue, applicant_found, self.applicants_list, self.artists_list)
    
    def open_artist_area(self, artist_found):
        """Open the admin area."""
        self.root.withdraw()  # Hide the login window
        ArtistArea(self.root, artist_found, self.requested_figures_queue)
