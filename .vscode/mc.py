import random

flashcards = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["CO2", "H2O", "NaCl", "CH4"],
        "answer": "H2O"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Donatello"],
        "answer": "Leonardo da Vinci"
    },
    # ... more flashcards
]

def play_flashcard_game():
    score = 0
    random.shuffle(flashcards)  # Shuffle the flashcards

    for flashcard in flashcards:
        print(flashcard["question"])

        # Display choices with letters:
        for i, choice in enumerate(flashcard["choices"]):
            print(f"{chr(65 + i)}. {choice}")

        while True:  # Loop until a valid input is received
            try:
                player_input = input("Enter the letter of your choice (A, B, C, or D): ").upper()
                if player_input in ["A", "B", "C", "D"]:
                    chosen_answer_index = ord(player_input) - ord('A')  # Convert letter to index
                    break  # Exit loop if input is valid
                else:
                    print("Invalid input. Please enter A, B, C, or D.")
            except ValueError:
                print("Invalid input. Please enter a letter.")

        chosen_answer = flashcard["choices"][chosen_answer_index]

        if chosen_answer.lower() == flashcard["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is: {flashcard['answer']}")

        print("-" * 20)  # Separator between questions

    print(f"Game Over! Your final score is: {score}")

play_flashcard_game()