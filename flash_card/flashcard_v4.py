import pygame
import time
import serial
import sys
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
HIGHLIGHT = (100, 100, 255)

# Font
font = pygame.font.Font(None, 36)

# Sample question and choices
# List of questions, each with its choices and the index of the correct answer
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

# Joystick control variables
selected_choice = 0

# Function to display the question and choices
def display_question():
    screen.fill(WHITE)
    question_surface = font.render(questions, True, BLACK)
    screen.blit(question_surface, (50, 50))
    for i, choice in enumerate(choices):
        color = HIGHLIGHT if i == selected_choice else BLACK
        choice_surface = font.render(choice, True, color)
        screen.blit(choice_surface, (50, 150 + i * 50))
    pygame.display.flip()

# Main game loop
running = True
while running:
    display_question()
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
        time.sleep(1)  # Pause before next question or action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.1)  # Adjust as needed

pygame.quit()
