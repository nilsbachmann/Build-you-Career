import subprocess
import sys
import os

def start_backend():
    backend_path = os.path.join(
        os.path.dirname(__file__),
        "backend",
        "src",
        "main",
        "main.py"
    )
    return subprocess.Popen([sys.executable, backend_path])

def start_frontend():
    frontend_path = os.path.join(
        os.path.dirname(__file__),
        "frontend",
        "main.py"
    )
    return subprocess.Popen([sys.executable, frontend_path])

if __name__ == "__main__":
    backend_proc = start_backend()
    frontend_proc = start_frontend()
    # Optional: Auf Prozesse warten
    frontend_proc.wait()
    backend_proc.terminate()