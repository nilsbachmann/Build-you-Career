import tkinter as tk
from home_screen import HomeScreen

class LoadingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)
        tk.Label(self, text="Lädt...", bg="white", fg="green", font=("Arial", 24)).pack(pady=100)
        self.after(1500, self.goto_home)

    def goto_home(self):
        self.pack_forget()
        HomeScreen(self.master)