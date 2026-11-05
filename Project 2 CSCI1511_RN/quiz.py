"""quiz.py, Robert Nance, the file for managing the quiz logic, 11/04/2026"""


from questions import select_questions
from messages import display_question


class Quiz:
    def __init__(self, question_bank, player, questions_per_round=3):
        self.question_bank = question_bank
        self.player = player
        self.questions_per_round = questions_per_round
        self.round_score = 0

    def check_answer(self, player_answer, correct_answer):
        """Check if the player's answer is correct."""
        return player_answer.upper() == correct_answer

    def run_quiz(self):
        """Run the quiz."""
        quiz_questions = select_questions(
            self.question_bank, 
            self.questions_per_round
        )

        self.round_score = 0

        for question in quiz_questions:
            display_question(question)
            
            answer = input("Enter your answer (A, B, C, or D): ")

            if self.check_answer(answer, question["answer"]):
                print("Correct!")
                self.round_score += 1
                self.player.record_correct_answer()
            else:
                print(f"Incorrect! The answer is {question['answer']}.")
                self.player.record_incorrect_answer()

        self.player.record_games_played()
        self.player.display_stats()
        return self.round_score

    def display_round_score(self):
        """Display the score for the current round."""
        print(f"You got {self.round_score} out of {self.questions_per_round} questions correct.")
    

