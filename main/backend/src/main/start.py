import os

def list_mods(mods_dir="mods"):
    """Listet verfügbare Mods im mods-Verzeichnis auf."""
    if not os.path.exists(mods_dir):
        print("Kein Mods-Ordner gefunden.")
        return []
    mods = [f for f in os.listdir(mods_dir) if f.endswith(".py")]
    if not mods:
        print("Keine Mods gefunden.")
    return mods

def load_mod(mod_name, mods_dir="mods"):
    """Lädt einen Mod dynamisch."""
    try:
        mod_path = f"{mods_dir}.{mod_name[:-3]}"
        __import__(mod_path)
        print(f"Mod '{mod_name}' geladen.")
    except Exception as e:
        print(f"Fehler beim Laden des Mods: {e}")

def start_singleplayer():
    print("Singleplayer wird gestartet...")
    # Hier kann die eigentliche Spiellogik eingefügt werden
    print("Viel Spaß im Singleplayer-Modus!")

def start_modded():
    mods = list_mods()
    if not mods:
        print("Starte ohne Mods.")
        start_singleplayer()
        return
    print("Verfügbare Mods:")
    for idx, mod in enumerate(mods, 1):
        print(f"{idx}. {mod}")
    choice = input("Wähle einen Mod (Nummer) oder Enter für keinen: ")
    if choice.isdigit() and 1 <= int(choice) <= len(mods):
        load_mod(mods[int(choice)-1])
    else:
        print("Kein Mod ausgewählt.")
    start_singleplayer()

def start_game():
    print("Bitte wähle einen Modus:")
    print("1. Singleplayer")
    print("2. Multiplayer (später verfügbar)")
    print("3. Modded")
    mode = input("Modus wählen (1-3): ")

    if mode == "1":
        print("Singleplayer wird gestartet...")
        return {"modus": "singleplayer", "spielstand": {}}
    elif mode == "2":
        print("Multiplayer ist noch nicht verfügbar.")
        return {"modus": "multiplayer", "spielstand": {}}
    elif mode == "3":
        print("Modded Modus ausgewählt.")
        # Hier könnte später eine Mod-Auswahl erfolgen
        return {"modus": "modded", "spielstand": {}}
    else:
        print("Ungültige Auswahl. Bitte erneut versuchen.")
        return start_game()