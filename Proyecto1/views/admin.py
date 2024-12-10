import tkinter as tk
import xml.etree.ElementTree as ET 
from tkinter import filedialog, messagebox
from utils.XMLHandler import XMLHandler

from ADT.app.ApplicantsList import ApplicantsList
from models.Applicant import Applicant

class AdminArea:
    def __init__(self, parent, applicants_list: ApplicantsList):
        self.parent = parent
        self.admin_window = tk.Toplevel()
        self.admin_window.title("Área de Administración")
        self.admin_window.geometry("600x400")

        self.file_pahts = ()
        self.applicants_list = applicants_list

        # Welcome label
        welcome_label = tk.Label(self.admin_window, text="Bienvenido al Área de Administración", font=("Arial", 16))
        welcome_label.pack(pady=30)

        # Load applicatns button
        load_applicants_button = tk.Button(self.admin_window, text='Cargar solicitantes', font=("Arial", 12), command=self.getFilePaths)
        load_applicants_button.pack(pady=30)

        # Logout button
        logout_button = tk.Button(self.admin_window, text="Cerrar sesión", font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        """Logout and return to the login window."""
        self.admin_window.destroy()
        self.parent.deiconify()

    def getFilePaths(self):
        self.file_paths = XMLHandler().getFilePaths()

        for file_path in self.file_paths:
            self.readFile(file_path)

    def readFile(self, file_path):
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
            
            self.applicants_list.append(newApplicant)
        
        self.applicants_list.printList()

    def load_applicants(self):
        file_paths = filedialog.askopenfilenames(
            title="Selecciona uno o más archivos XML",
            filetypes=(("Archivos XML", "*.xml"), ("Todos los archivos", "*.*"))
        )
        if file_paths:
            file_list.delete("1.0", tk.END)  # Clear previous content
            for file_path in file_paths:
                try:
                    tree = ET.parse(file_path)  # Parse the XML file
                    root = tree.getroot()  # Get the root element

                    # Display the file name and its XML structure
                    file_list.insert(tk.END, f"--- {file_path} ---\n")
                    file_list.insert(tk.END, format_xml(root) + "\n\n")
                except ET.ParseError as e:
                    messagebox.showerror("Error", f"Error al parsear el archivo {file_path}:\n{e}")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo abrir el archivo {file_path}:\n{e}")

            print(file_list)
        else:
            messagebox.showinfo("Cancelado", "No se seleccionaron archivos")