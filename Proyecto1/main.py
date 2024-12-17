import tkinter as tk
from tkinter import messagebox

from views.LoginArea import LoginApp

from ADT.Queue import Queue
from ADT.app.ApplicantsList import ApplicantsList
from ADT.app.ArtistsList import ArtistsList

# Main application
if __name__ == "__main__":
    root = tk.Tk()

    # Data persistence
    requested_figures_queue = Queue()
    applicants_list = ApplicantsList()
    artists_list = ArtistsList()

    app = LoginApp(
        root, 
        requested_figures_queue,
        applicants_list,
        artists_list
    )

    root.mainloop()