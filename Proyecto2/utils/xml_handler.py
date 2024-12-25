from tkinter import filedialog

class XMLHandler:

    def __init__(self):
        self.file_paths = None
        self.openFinder()

    def openFinder(self):
        try:
            self.file_paths = filedialog.askopenfilenames(
                title="Selecciona uno o más archivos XML",
                filetypes=(("Archivos XML", "*.xml"), ("Todos los archivos", "*.*"))
            )

            if not self.file_paths:
                self.file_paths = None
        except Exception as e:
            print(f'Error: {e}')

    def getFilePaths(self):
        return self.file_paths