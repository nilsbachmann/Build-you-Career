# Beispiel: Importiere Spiellogik-Module
from logic.simulation import run_simulation
from logic.economy import update_economy
from logic.career import progress_career

def execute_game_logic(game_state, player_action):
    """Führt die Hauptlogik des Spiels aus."""
    # Simulationslogik
    game_state = run_simulation(game_state, player_action)
    # Wirtschaftssimulation
    game_state = update_economy(game_state)
    # Karrierefortschritt
    game_state = progress_career(game_state, player_action)
    return game_state