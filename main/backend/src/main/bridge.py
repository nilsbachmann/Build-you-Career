from logicgate import execute_game_logic

def handle_frontend_request(request_data):
    game_state = request_data.get("game_state")
    player_action = request_data.get("player_action")
    updated_state = execute_game_logic(game_state, player_action)
    return {"game_state": updated_state}