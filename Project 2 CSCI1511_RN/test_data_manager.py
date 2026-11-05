"""test_data_manager.py, Robert Nance, the file for testing the data manager, 11/04/2026"""

import json

from player import Player
from data_manager import load_player_data, save_player_data


def test_load_player_data(tmp_path):
    """Test that saved player data can be loaded from a JSON file."""

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
    """Test that a missing JSON file returns an empty dictionary."""

    file_path = tmp_path / "missing.json"

    loaded_data = load_player_data(file_path)

    assert loaded_data == {}


def test_load_invalid_json(tmp_path, capsys):
    """Test that invalid JSON is handled without crashing."""

    file_path = tmp_path / "invalid.json"

    file_path.write_text(
        "{invalid json",
        encoding="utf-8"
    )

    loaded_data = load_player_data(file_path)

    captured = capsys.readouterr()

    assert loaded_data == {}
    assert "corrupted" in captured.out


def test_load_invalid_data_format(tmp_path, capsys):
    """Test that JSON with the wrong data structure is rejected."""

    file_path = tmp_path / "invalid_format.json"

    file_path.write_text(
        json.dumps(["TestPlayer", "AnotherPlayer"]),
        encoding="utf-8"
    )

    loaded_data = load_player_data(file_path)

    captured = capsys.readouterr()

    assert loaded_data == {}
    assert "invalid format" in captured.out


def test_save_player_data(tmp_path):
    """Test that a player's statistics can be saved to a JSON file."""

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
    """Test that saving another player preserves existing player data."""

    file_path = tmp_path / "quiz_data.json"

    first_player = Player("TestPlayer", 8, 4, 4)
    second_player = Player("AnotherPlayer", 5, 7, 3)

    save_player_data(first_player, file_path)
    save_player_data(second_player, file_path)

    saved_data = load_player_data(file_path)

    assert "TestPlayer" in saved_data
    assert "AnotherPlayer" in saved_data

    assert saved_data["TestPlayer"]["correct_answers"] == 8
    assert saved_data["AnotherPlayer"]["correct_answers"] == 5