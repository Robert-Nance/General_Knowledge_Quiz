"""test_player.py, Robert Nance, the file for testing the player class, 11/04/2026"""

from player import Player

def test_player_initialization():
    player = Player("TestPlayer")
    assert player.name == "TestPlayer"
    assert player.correct_answers == 0
    assert player.incorrect_answers == 0
    assert player.games_played == 0

def test_record_correct_answer():
    player = Player("TestPlayer")
    player.record_correct_answer()
    assert player.correct_answers == 1

def test_record_incorrect_answer():
    player = Player("TestPlayer")
    player.record_incorrect_answer()
    assert player.incorrect_answers == 1

def test_record_games_played():
    player = Player("TestPlayer")
    player.record_games_played()
    assert player.games_played == 1

def test_calculate_score():
    player = Player("TestPlayer")
    player.record_correct_answer()
    player.record_correct_answer()
    player.record_correct_answer()
    assert player.calculate_score() == 3

def test_restore_saved_stats():
    player = Player("TestPlayer", 8, 4, 4)
    assert player.correct_answers == 8
    assert player.incorrect_answers == 4
    assert player.games_played == 4
