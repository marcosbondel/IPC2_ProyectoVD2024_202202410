import tkinter as tk
from tkinter import messagebox
from views.Login import LoginApp


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()