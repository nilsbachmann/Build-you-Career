import tkinter as tk
from pause_screen import PauseScreen

# Backend-Importe
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main', 'backend', 'src', 'main')))
from bridge import handle_frontend_request

class GameScreen(tk.Frame):
    def __init__(self, master, initial_state=None):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)
        self.game_state = initial_state or {"modus": "singleplayer", "spielstand": {}}

        self.status_label = tk.Label(self, text="Spiel läuft...", bg="white", fg="green", font=("Arial", 20))
        self.status_label.pack(pady=20)

        self.info_label = tk.Label(self, text="", bg="white", fg="green", font=("Arial", 12))
        self.info_label.pack(pady=10)

        self.action_entry = tk.Entry(self, font=("Arial", 14))
        self.action_entry.pack(pady=10)
        self.action_entry.insert(0, "arbeiten")

        tk.Button(self, text="Aktion ausführen", bg="green", fg="white", command=self.do_action).pack(pady=5)
        tk.Button(self, text="Pause", bg="green", fg="white", command=self.pause).pack(pady=5)

        self.update_status()

    def do_action(self):
        action = self.action_entry.get()
        if action == "beenden":
            self.master.quit()
            return
        request_data = {
            "game_state": self.game_state,
            "player_action": action
        }
        response = handle_frontend_request(request_data)
        self.game_state = response.get("game_state", self.game_state)
        self.update_status()

    def update_status(self):
        # Zeige den aktuellen Spielstatus an
        status = "\n".join([f"{k}: {v}" for k, v in self.game_state.items()])
        self.info_label.config(text=status)

    def pause(self):
        self.pack_forget()
        PauseScreen(self.master, self.game_state)