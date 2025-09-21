# Beispielhafte Konfigurationen für das Spiel

DEFAULT_CONFIG = {
    "start_geld": 1000,
    "max_karriere_level": 10,
    "mod_support": True
}

def get_config(key, default=None):
    return DEFAULT_CONFIG.get(key, default)