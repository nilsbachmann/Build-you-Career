import tkinter as tk
from game_screen import GameScreen

# Backend-Import
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main', 'backend', 'src', 'main')))
from start import start_game

class ChooseScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)
        tk.Label(self, text="Modus wählen", bg="white", fg="green", font=("Arial", 20)).pack(pady=40)
        tk.Button(self, text="Singleplayer", bg="green", fg="white", command=self.start_game).pack(pady=10)
        tk.Button(self, text="Zurück", bg="green", fg="white", command=self.goto_home).pack(pady=10)

    def start_game(self):
        initial_state = start_game()
        self.pack_forget()
        GameScreen(self.master, initial_state)

    def goto_home(self):
        from home_screen import HomeScreen
        self.pack_forget()
        HomeScreen(self.master)