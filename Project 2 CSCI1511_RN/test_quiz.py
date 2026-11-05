"""test_quiz.py, Robert Nance, the file for testing the quiz logic, 11/04/2026"""

from player import Player
from quiz import Quiz

def test_check_answer_correct():
    player = Player("TestPlayer")
    quiz = Quiz([], player)
    assert quiz.check_answer("A", "A") is True

def test_check_answer_incorrect():
    player = Player("TestPlayer")
    quiz = Quiz([], player)
    assert quiz.check_answer("A", "B") is False

def test_run_quiz(monkeypatch):
    player = Player("TestPlayer")

    question_bank = [
        {
            "question": "What is the capital of Texas?",
            "options": ["A. Austin", "B. Dallas"],
            "answer": "A"
        },
        {
            "question": "What is the capital of California?",
            "options": ["A. Sacramento", "B. Los Angeles"],
            "answer": "A"
        }
    ]

    quiz = Quiz(question_bank, player, 2)

    monkeypatch.setattr(
        "quiz.select_questions",
        lambda bank, number: question_bank
    )

    monkeypatch.setattr(
        "quiz.display_question",
        lambda question: None
    )

    answers = iter(["A", "B"])

    monkeypatch.setattr(
        "builtins.input", 
        lambda prompt: next(answers)
    )

    score = quiz.run_quiz()

    assert score == 1
    assert player.correct_answers == 1
    assert player.incorrect_answers == 1
    assert player.games_played == 1

def test_round_score_resets(monkeypatch):
    player = Player("TestPlayer")

    question_bank = [
        {
            "question": "What is the capital of Texas?",
            "options": ["A. Austin", "B. Dallas"],
            "answer": "A"
        }
    ]

    quiz = Quiz(question_bank, player, 1)

    monkeypatch.setattr(
        "quiz.select_questions",
        lambda bank, number: question_bank
    )

    monkeypatch.setattr(
        "quiz.display_question",
        lambda question: None
    )

    answers = iter(["A", "B"])

    monkeypatch.setattr(
        "builtins.input", 
        lambda prompt: next(answers)
    )

    first_score = quiz.run_quiz()
    second_score = quiz.run_quiz()

    assert first_score == 1
    assert second_score == 0
    assert player.correct_answers == 1
    assert player.incorrect_answers == 1
    assert player.games_played == 2

def test_display_round_score(capsys):
    player = Player("TestPlayer")

    quiz = Quiz([], player)
    quiz.round_score = 2
    quiz.display_round_score()
    captured = capsys.readouterr()
    assert "You got 2 out of 3 questions correct." in captured.out