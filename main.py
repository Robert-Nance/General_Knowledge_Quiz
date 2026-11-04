

from questions import questions
from messages import welcome_player, goodbye_player
from quiz import Quiz
from player import Player

def main():
    """Start the quiz."""

    player_name = input("Enter your name: ")
    
    player = Player(player_name)

    quiz = Quiz(questions, player, 3)

    welcome_player(player_name)

    play_again = True

    while play_again:

        quiz.run_quiz()

        quiz.display_round_score()

        answer = input("Do you want to play again? (yes/no): ")
        if answer != "yes":
            play_again = False

    player.display_stats()

    goodbye_player(player.name)
        
if __name__ == "__main__":
    main()