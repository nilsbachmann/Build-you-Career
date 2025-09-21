import tkinter as tk
from loading_screen import LoadingScreen

def start_frontend():
    root = tk.Tk()
    root.title("Build your Career")
    root.configure(bg="white")
    app = LoadingScreen(root)
    root.mainloop()

if __name__ == "__main__":
    start_frontend()