def progress_career(game_state, player_action):
    # Beispiel: Karrierefortschritt simulieren
    if player_action == "arbeiten":
        game_state["karriere_level"] = game_state.get("karriere_level", 1) + 1
    return game_state