import tkinter as tk
from game_screen import GameScreen
from home_screen import HomeScreen

class PauseScreen(tk.Frame):
    def __init__(self, master, game_state):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)
        self.game_state = game_state
        tk.Label(self, text="Pause", bg="white", fg="green", font=("Arial", 20)).pack(pady=40)
        tk.Button(self, text="Weiter", bg="green", fg="white", command=self.resume).pack(pady=10)
        tk.Button(self, text="Zum Hauptmenü", bg="green", fg="white", command=self.goto_home).pack(pady=10)

    def resume(self):
        self.pack_forget()
        GameScreen(self.master, self.game_state)

    def goto_home(self):
        self.pack_forget()
        HomeScreen(self.master)