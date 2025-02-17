import pygame
import serial
import time
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joystick-Controlled Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (100, 100, 255)

# Font
font = pygame.font.Font(None, 36)

# Questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "London", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["3", "4", "5", "6"],
        "answer": 1
    },
    # Add more questions as needed
]

# Serial port configuration
try:
    ser = serial.Serial('COM5', 9600, timeout=1)  # Adjust 'COM3' as needed
except serial.SerialException:
    print("Error: Could not open serial port.")
    sys.exit()

def read_joystick():
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            x, y, sw = map(int, line.split(','))
            return x, y, sw
    except:
        pass
    return None

def display_question(question, choices, selected):
    screen.fill(WHITE)
    question_text = font.render(question, True, BLACK)
    screen.blit(question_text, (50, 50))
    for i, choice in enumerate(choices):
        color = HIGHLIGHT if i == selected else BLACK
        choice_text = font.render(choice, True, color)
        screen.blit(choice_text, (100, 150 + i * 50))
    pygame.display.flip()

def run_quiz():
    current_question = 0
    selected_choice = 0
    clock = pygame.time.Clock()
    while current_question < len(questions):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                ser.close()
                sys.exit()
        joystick_data = read_joystick()
        if joystick_data:
            x, y, sw = joystick_data
            if ser.readline().decode:  # Adjust threshold as needed
                selected_choice = (selected_choice - 1) % 4
                time.sleep(0.2)  # Debounce delay
            elif y > 600:  # Adjust threshold as needed
                selected_choice = (selected_choice + 1) % 4
                time.sleep(0.2)  # Debounce delay
            if sw == 0:  # Joystick button pressed
                if selected_choice == questions[current_question]["answer"]:
                    print("Correct!")
                else:
                    print("Incorrect.")
                current_question += 1
                selected_choice = 0
                time.sleep(0.5)  # Delay before next question
        if current_question < len(questions):
            q = questions[current_question]
            display_question(q["question"], q["choices"], selected_choice)
        clock.tick(30)

if __name__ == "__main__":
    run_quiz()
