import zipfile
import os
import importlib.util

MODS_DIR = "mods"

def extract_mod(zip_path):
    """Extrahiert eine Mod-ZIP-Datei ins Mods-Verzeichnis."""
    if not os.path.exists(MODS_DIR):
        os.makedirs(MODS_DIR)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(MODS_DIR)
    print(f"Mod aus {zip_path} extrahiert.")

def load_mod(mod_name):
    """Lädt ein Mod-Python-Modul aus dem Mods-Verzeichnis."""
    mod_path = os.path.join(MODS_DIR, mod_name, "__init__.py")
    if not os.path.isfile(mod_path):
        print(f"Modul {mod_name} nicht gefunden.")
        return None
    spec = importlib.util.spec_from_file_location(mod_name, mod_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f"Modul {mod_name} geladen.")
    return mod

def list_mods():
    """Listet alle verfügbaren Mods im Mods-Verzeichnis auf."""
    if not os.path.exists(MODS_DIR):
        return []
    return [name for name in os.listdir(MODS_DIR) if os.path.isdir(os.path.join(MODS_DIR, name))]