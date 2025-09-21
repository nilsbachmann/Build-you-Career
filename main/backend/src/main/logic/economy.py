def update_economy(game_state):
    # Beispiel: Wirtschaftliche Veränderungen simulieren
    game_state["geld"] = game_state.get("geld", 1000) + 10
    return game_state