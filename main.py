

from questions import questions
from messages import welcome_player, goodbye_player
from quiz import run_quiz, play_again

def main():
    """Start the quiz."""

    player_name = input("Enter your name: ")

    welcome_player(player_name)

    play_again = True

    while play_again:
        score = run_quiz(questions, 3)

        print(f"You got {score} out of 3 questions correct.")

        replay = play_again()

    goodbye_player(player_name)

if __name__ == "__main__":
    main()