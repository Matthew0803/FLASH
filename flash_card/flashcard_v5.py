import pygame
import sys
import random
import time
import serial

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiple Choice Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

def read_joystick():
    try:
        with serial.Serial('COM5', 9600, timeout=1) as ser:  # Update 'COM3' to your Arduino's serial port
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        return line  # Return the direction or 'SELECT' command
    except serial.SerialException:
        print("Error: Could not open serial port.")
        sys.exit()

# Questions list
questions = [
    {
        "question": "What is the largest internal organ in the human body?",
        "choices": ["A) Lungs", "B) Heart", "C) Kidneys", "D) Liver"],
        "correct_answer": 3  # Index of the correct answer
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "correct_answer": 1
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["A) Charles Dickens", "B) Jane Austen", "C) William Shakespeare", "D) Mark Twain"],
        "correct_answer": 2
    },
    {
        "question": "What is the capital city of Japan?",
        "choices": ["A) Beijing", "B) Seoul", "C) Bangkok", "D) Tokyo"],
        "correct_answer": 3
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oganesson"],
        "correct_answer": 1
    },
    {
        "question": "In which year did the Titanic sink?",
        "choices": ["A) 1905", "B) 1912", "C) 1918", "D) 1923"],
        "correct_answer": 1
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "correct_answer": 2
    },
    {
        "question": "Which planet is closest to the Sun?",
        "choices": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
        "correct_answer": 2
    },
    {
        "question": "Who painted the 'Mona Lisa'?",
        "choices": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "correct_answer": 2
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
        "correct_answer": 2
    }
]

# Shuffle questions to present them in random order
random.shuffle(questions)

# Function to display text on the screen
def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def main():
    current_question_index = 0
    score = 0
    selected_choice = -1  # No choice selected initially

    while current_question_index < len(questions):
        command = read_joystick()
        if command == "UP":
            selected_choice = (selected_choice - 1) % len(choices)
        elif command == "DOWN":
            selected_choice = (selected_choice + 1) % len(choices)
        elif command == "RIGHT":
            if selected_choice == correct_answer:
                print("Correct!")
        else:
            print("Incorrect.")
        time.sleep(1)
        current_question_index += 1
        selected_choice = -1  # Reset selection for next question

        screen.fill(WHITE)

        if current_question_index < len(questions):
            question = questions[current_question_index]
            display_text(question["question"], 50, 50)

            for i, choice in enumerate(question["choices"]):
                color = BLUE if i == selected_choice else BLACK
                display_text(choice, 100, 150 + i * 40, color)
        else:
            display_text(f"Quiz Over! Your score: {score}/{len(questions)}", 50, 50)

        pygame.display.flip()

    # Wait for a few seconds before quitting
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
