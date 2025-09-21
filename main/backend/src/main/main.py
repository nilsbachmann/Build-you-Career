from start import start_game
from bridge import handle_frontend_request

def main():
    print("Willkommen zu Build your Career!")
    initial_state = start_game()
    game_state = initial_state

    while True:
        action = input("Was möchtest du tun? (z.B. 'arbeiten', 'lernen', 'beenden'): ")
        if action == "beenden":
            print("Spiel wird beendet.")
            break

        request_data = {
            "game_state": game_state,
            "player_action": action
        }
        response = handle_frontend_request(request_data)
        game_state = response.get("game_state", game_state)
        print("Aktueller Spielstatus:", game_state)

if __name__ == "__main__":
    main()