import random

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    # ... more flashcards
]
# ... (flashcards data as defined above)

def play_flashcard_game():
    score = 0
    random.shuffle(flashcards)  # Shuffle the flashcards

    for flashcard in flashcards:
        print(flashcard["question"]) # Display on the robot's screen
        player_answer = input("Your answer: ") # Get input (replace with robot input method)

        if player_answer.lower() == flashcard["answer"].lower(): # Case-insensitive comparison
            print("Correct!") # Display on robot screen
            score += 1
        else:
            print(f"Incorrect. The answer is: {flashcard['answer']}") # Display on robot screen

    print(f"Game Over! Your final score is: {score}") # Display on robot screen

play_flashcard_game()

