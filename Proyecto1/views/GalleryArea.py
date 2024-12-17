import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from models.Applicant import Applicant

images = ["image1.jpg", "image2.jpg", "image3.jpg"]

class GalleryArea:
    def __init__(self, parent, applicant: Applicant):
        self.parent = parent
        self.gallery_window = tk.Toplevel()
        self.gallery_window.title("Galeria")
        self.gallery_window.geometry("500x600")


        self.current_figure = None
        self.applicant_session = applicant
        
        if self.applicant_session.accepted_figures.len() > 0:
            self.current_figure = self.applicant_session.accepted_figures.first()

        self.load_image()

        # "Previous" button
        self.prev_button = ttk.Button(self.gallery_window, text="Atras", command=self.previous_image)
        self.prev_button.grid(row=1, column=0, padx=10)

        # "Next" button
        self.next_button = ttk.Button(self.gallery_window, text="Siguiente", command=self.next_image)
        self.next_button.grid(row=1, column=2, padx=10)
        
        # "Exit" button
        self.exit_button = ttk.Button(self.gallery_window, text="Cerrar", command=self.close)
        self.exit_button.grid(row=2, column=2, padx=10)


    def close(self):
        """Logout and return to the login window."""
        self.gallery_window.destroy()
        self.parent.deiconify()

    def load_image(self):

        if not self.current_figure:
            return

        # Load the image
        # img = Image.open(images[self.current_index])
        img = Image.open(f'Proyecto1/reports/matrix_{self.current_figure.value.bId}.png')
        # img = img.resize((400, 300), Image.ANTIALIAS)  # Resize the image
        img = img.resize((500, 500), Image.Resampling.LANCZOS)  # Resize the image

        self.img_tk = ImageTk.PhotoImage(img)

        # Display the image in a Label
        if hasattr(self, "image_label"):
            self.image_label.configure(image=self.img_tk)
        else:
            self.image_label = ttk.Label(self.gallery_window, image=self.img_tk)
            self.image_label.grid(row=0, column=0, columnspan=3)

    def previous_image(self):
        # Move to the previous image
        if self.current_figure.previousValue:
            self.current_figure = self.current_figure.previousValue
        self.load_image()

    def next_image(self):
        # Move to the next image
        if self.current_figure.nextValue:
            self.current_figure = self.current_figure.nextValue
        self.load_image()