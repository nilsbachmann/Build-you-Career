import tkinter as tk
from choose_screen import ChooseScreen

class HomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)
        tk.Label(self, text="Willkommen!", bg="white", fg="green", font=("Arial", 24)).pack(pady=40)
        tk.Button(self, text="Spiel starten", bg="green", fg="white", command=self.goto_choose).pack(pady=10)
        tk.Button(self, text="Beenden", bg="green", fg="white", command=master.quit).pack(pady=10)

    def goto_choose(self):
        self.pack_forget()
        ChooseScreen(self.master)