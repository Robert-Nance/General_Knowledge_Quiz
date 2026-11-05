

import json

def load_player_data(filename="player_data.json"):
    """Load player data from a JSON file."""
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            print("Error: JSON file has an invalid format.")
            return {}
        
        return data

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return {}

def save_player_data(player, filename="quiz_data.json"):
    """Save player data to a JSON file."""
    
    data = load_player_data(filename)
    
    data[player.name] = {
        "correct_answers": player.correct_answers,
        "incorrect_answers": player.incorrect_answers,
        "games_played": player.games_played
    }

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError as error:
        print(f"Unable to save player data: {error}")
        return False