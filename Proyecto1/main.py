import tkinter as tk
from tkinter import messagebox

# Función para manejar el inicio de sesión
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login", "Inicio de sesión exitoso")
        open_admin_area()
    else:
        messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")

# Función para abrir el área de administración
def open_admin_area():
    # Ocultar la ventana principal
    root.withdraw()

    # Crear la ventana de administración
    admin_window = tk.Toplevel()
    admin_window.title("Área de Administración")
    admin_window.geometry("600x400")

    # Etiqueta de bienvenida
    welcome_label = tk.Label(admin_window, text="Bienvenido al Área de Administración", font=("Arial", 16))
    welcome_label.pack(pady=30)

    # Botón para cerrar sesión
    logout_button = tk.Button(admin_window, text="Cerrar sesión", font=("Arial", 12), command=lambda: close_admin_area(admin_window))
    logout_button.pack(pady=20)

# Función para cerrar el área de administración y regresar al login
def close_admin_area(admin_window):
    admin_window.destroy()
    root.deiconify()

# Crear ventana principal
root = tk.Tk()
root.title("Login")
root.geometry("500x300")  # Ajustar el tamaño de la ventana
root.resizable(False, False)

# Crear un marco para centralizar el contenido
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Etiqueta de título
title_label = tk.Label(frame, text="Sistema de Login", font=("Arial", 18))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Etiqueta y entrada para el nombre de usuario
username_label = tk.Label(frame, text="Usuario:", font=("Arial", 12))
username_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")

username_entry = tk.Entry(frame, font=("Arial", 12), width=30)
username_entry.grid(row=1, column=1, pady=10, padx=10)

# Etiqueta y entrada para la contraseña
password_label = tk.Label(frame, text="Contraseña:", font=("Arial", 12))
password_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")

password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
password_entry.grid(row=2, column=1, pady=10, padx=10)

# Botón para iniciar sesión
login_button = tk.Button(frame, text="Iniciar sesión", font=("Arial", 12), width=15, command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Botón para salir
exit_button = tk.Button(frame, text="Salir", font=("Arial", 12), width=15, command=root.quit)
exit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
