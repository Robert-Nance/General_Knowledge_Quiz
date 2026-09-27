
"""the import random allows me to pull random questions from the dictionary of questions"""

import random

"""initialize the quiz with the player's name"""

player_name = input("Enter your name: ")
print(f"Welcome, {player_name}! Good luck!")

"""The list of questions the quiz is pulling from"""

questions = [
    {
        "question": "What is the capital of Ohio?", 
     "options": ["A) Columbus", "B) Cleveland", "C) Cincinnati", "D) Sandusky"], 
     "answer": "A"
     },
    {
        "question": "What is the largest unit of measurement listed here?",
          "options": ["A) Inch", "B) Meter", "C) Mile", "D) Foot"], 
          "answer": "C"
          },
    {
        "question": "Who wrote 'Romeo and Juliet'?", 
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"], 
        "answer": "B"
        },
    {
        "question": "What is Mario's brother's name?",
        "options": ["A) Larry", "B) Lemmy", "C) Loogy", "D) Luigi"],
        "answer": "D"
    },
    {
        "question": "What year did the PlayStation 5 release?",
        "options": ["A) 2020", "B) 2019", "C) 2021", "D) 2022"],
        "answer": "A"
    },
    {
        "question": "Who was the second president of the United States?",
        "options": ["A) George Washington", "B) Thomas Jefferson", "C) John Adams", "D) James Madison"],
        "answer": "C"
    },
    {
        "question": "Where is Mount Rushmore located?",
        "options": ["A) South Dakota", "B) North Dakota", "C) Montana", "D) Wyoming"],
        "answer": "A"
    },
    {
        "question": "How many units did the Nintendo Wii sell worldwide?",
        "options": ["A) 50 million", "B) 100 million", "C) 200 million", "D) 150 million"],
        "answer": "B"
    },
    {
        "question": "Which famous Youtuber was known to live in Cincinnati, Ohio, before moving to California?",
        "options": ["A) DanTDM", "B) PewDiePie", "C) Markiplier", "D) Jacksepticeye"],
        "answer": "C"
    },
    {
        "question": "Who does the player control in the Legend of Zelda: Breath of the Wild?",
        "options": ["A) Sheik", "B) Zelda", "C) Ganon", "D) Link"],
        "answer": "D"
    }
]

"""Ask the player if they want to play again after the quiz is over"""

play_again = True

while play_again:
    quiz = random.sample(questions, 3)

    for question in quiz:
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").upper()

        if answer == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.")

    play_again_answer = input("Do you want to play again? (yes/no): ").lower()

    if play_again_answer != "yes":
        play_again = False

print(f"Thanks for playing, {player_name}!")