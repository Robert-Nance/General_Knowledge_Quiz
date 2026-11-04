
from questions import select_questions
from messages import display_question

def check_answer(player_answer, correct_answer):
    """Check if the player's answer is correct."""
    return player_answer.upper() == correct_answer

def run_quiz(question_bank, number_of_questions):
    """Run the quiz."""

    quiz_questions = select_questions(
        question_bank, number_of_questions
    )

    correct_answers = 0

    for question in quiz_questions:
        display_question(question)
        answer = input("Enter your answer (A, B, C, or D): ")

        if check_answer(answer, question["answer"]):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The answer is {question['answer']}.")

    return correct_answers

def play_again():
    """Ask the player if they want to play again."""
    answer = input("Do you want to play again? (yes/no): ")

    return answer == "yes"

