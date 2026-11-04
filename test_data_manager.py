

import json

from player import Player
from data_manager import load_player_data, save_player_data

def test_load_player_data():
    file_path = tmp_path / "quiz_data.json"
    
    expected_data = {
        "TestPlayer": {
            "correct_answers": 8,
            "incorrect_answers": 4,
            "games_played": 4
        }
    }

    file_path.write_text(
        json.dumps(expected_data),
        encoding="utf-8"
    )

    loaded_data = load_player_data(file_path)

    assert loaded_data == expected_data

def test_load_missing_file(tmp_path):
    file_path = tmp_path / "non_existent_file.json"

    file_path.write_text(
        "{invalid json",
        encoding="utf-8"
    )

    loaded_data = load_player_data(file_path)

    captured = capsys.readouterr()

    assert loaded_data == {}
    assert "Error: JSON file is corrupted." in captured.out

def test_load_corrupted_file(tmp_path, capsys):
    file_path = tmp_path / "corrupted_file.json"

    file_path.write_text(
        json.dumps(["TestPlayer", "TestPlayer2"]),
        encoding="utf-8"
    )

    loaded_data = load_player_data(file_path)

    captured = capsys.readouterr()

    assert loaded_data == {}
    assert "invalid format" in captured.out

def test_save_player_data(tmp_path):
    file_path = tmp_path / "quiz_data.json"

    player = Player("TestPlayer", 8, 4, 4)

    result = save_player_data(player, file_path)

    saved_data = json.loads(
        file_path.read_text(encoding="utf-8")
    )

    assert result is True
    assert saved_data["TestPlayer"]["correct_answers"] == 8
    assert saved_data["TestPlayer"]["incorrect_answers"] == 4
    assert saved_data["TestPlayer"]["games_played"] == 4

def test_save_multiple_players(tmp_path):
    file_path = tmp_path / "quiz_data.json"

    player1 = Player("TestPlayer1", 8, 4, 4)
    player2 = Player("TestPlayer2", 5, 7, 3)

    save_player_data(player1, file_path)
    save_player_data(player2, file_path)

    saved_data = load_player_data(file_path)

    assert "TestPlayer1" in saved_data
    assert "TestPlayer2" in saved_data

    assert saved_data["TestPlayer1"]["correct_answers"] == 8
    assert saved_data["TestPlayer2"]["correct_answers"] == 5