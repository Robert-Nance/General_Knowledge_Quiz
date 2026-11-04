

class Player:
    """Represents the player..."""

    def __init__(self, name):
        self.name = name
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.games_played = 0

    def record_correct_answer(self):
        """Increment the count of correct answers."""
        self.correct_answers += 1

    def record_incorrect_answer(self):
        """Increment the count of incorrect answers."""
        self.incorrect_answers += 1

    def record_games_played(self):
        """Increment the count of games played."""
        self.games_played += 1

    def calculate_score(self):
        """Return number of correct answers."""
        return self.correct_answers

    def display_stats(self):
        """Display the player's statistics."""
        print(f"\nPlayer: {self.name}")
        print(f"Correct Answers: {self.correct_answers}")
        print(f"Incorrect Answers: {self.incorrect_answers}")
        print(f"Games Played: {self.games_played}")
        print(f"Score: {self.calculate_score()}")