"""messages.py, Robert Nance, the file for displaying messages, 11/04/2026"""

def welcome_player(player_name):
    """Display welcome message."""
    print(f"Welcome, {player_name}! Good luck!")

def goodbye_player(player_name):
    """Display goodbye message."""
    print(f"Thanks for playing, {player_name}! Goodbye!")

def display_question(question):
    """Display question and options."""
    print(question["question"])
    
    for option in question["options"]:
        print(option)