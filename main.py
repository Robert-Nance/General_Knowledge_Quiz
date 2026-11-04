

from questions import questions
from messages import welcome_player, goodbye_player
from quiz import Quiz
from player import Player
from data_manager import load_player_data, save_player_data

def main():
    """Start the quiz."""

    player_name = input("Enter your name: ")

    saved_data = load_player_data()

    player_stats = saved_data.get(player_name, {})
    
    player = Player(
        player_name, 
        player_stats.get("correct_answers", 0),
        player_stats.get("incorrect_answers", 0),
        player_stats.get("games_played", 0)
    )

    quiz = Quiz(questions, player, 3)

    welcome_player(player_name)

    play_again = True

    while play_again:

        quiz.run_quiz()

        quiz.display_round_score()

        save_player_data(player)

        answer = input("Do you want to play again? (yes/no): ")
        if answer != "yes":
            play_again = False

    player.display_stats()

    goodbye_player(player.name)
        
if __name__ == "__main__":
    main()