import pygame
import os
import time
import json
import serial
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 177, 76)
RED = (255, 99, 71)
YELLOW = (255, 255, 0)

# Game Settings
WIDTH, HEIGHT = 600, 800
FPS = 10
FONT = pygame.font.Font(None, 36)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flashcard Game")

# Create clock
clock = pygame.time.Clock()

# Load flashcards from JSON file
def load_flashcards(filename):
    with open(filename, "r") as file:
        return json.load(file)

flashcards = load_flashcards("flashcards.json")

# Game Variables
score = 0
question_index = 0
selected_answer = None
is_answered = False
is_game_over = False
showing_gif = False
gif_index = 0
answer_time = None
highlight_index = 0  # Initialize highlight index

# Load GIF frames
def load_gif(folder):
    frames = []
    if os.path.exists(folder):
        for filename in sorted(os.listdir(folder)):  # Ensure frames are loaded in order
            if filename.endswith(".png"):
                frame = pygame.image.load(os.path.join(folder, filename))
                frames.append(frame)
    return frames

correct_frames = load_gif("correct_gif")
incorrect_frames = load_gif("incorrect_gif")

# Function to display text
def display_text(text, font, color, x, y, center=False):
    label = font.render(text, True, color)
    if center:
        x = WIDTH // 2 - label.get_width() // 2
    screen.blit(label, (x, y))

# Function to draw answer buttons
def draw_buttons(options, highlight_index=None):
    button_height = 50  
    button_width = 500
    y_offset = 550  
    radius = 20  

    for idx, option in enumerate(options):
        color = BLUE
        if idx == highlight_index:
            color = GREEN  # Highlight correct selection
        pygame.draw.rect(screen, color, (50, y_offset + idx * (button_height + 10), button_width, button_height), border_radius=radius)
        display_text(option, FONT, WHITE, 75, y_offset + idx * (button_height + 10) + 10)

# Function to move to the next question
def next_question():
    global question_index, is_answered, selected_answer, showing_gif, gif_index, is_game_over, answer_time, highlight_index
    
    question_index += 1
    if question_index >= len(flashcards):
        is_game_over = True
    else:
        is_answered = False
        selected_answer = None
        showing_gif = False
        gif_index = 0
        answer_time = None
        highlight_index = 0 # Reset highlight index

# Serial communication setup
try:
    ser = serial.Serial('COM5', 9600)  # Replace 'COM5' with your Arduino's serial port
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    sys.exit() # Proper exit on serial error


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if is_game_over:
        display_text(f"Game Over! Final Score: {score}", FONT, YELLOW, WIDTH // 2, 180, center=True)

    else:
        question_data = flashcards[question_index]
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct"]

        display_text(question, FONT, YELLOW, WIDTH // 2, 50, center=True)

        if not is_answered:
            draw_buttons(options, highlight_index)  # Initial drawing

        else:
            if showing_gif:
                if gif_index < len(correct_frames):  
                    frame = correct_frames[gif_index] if selected_answer == correct_answer else incorrect_frames[gif_index]
                    screen.blit(frame, frame.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
                    gif_index += 1  

                if selected_answer == correct_answer:
                    display_text("Correct!", FONT, GREEN, WIDTH // 2, HEIGHT // 2 + 115, center=True)
                else:
                    display_text("Incorrect!", FONT, RED, WIDTH // 2, HEIGHT // 2 + 80, center=True)

                display_text(f"Correct Answer: {correct_answer}", FONT, YELLOW, WIDTH // 2, HEIGHT // 2 + 140, center=True)


                if answer_time is None:
                    answer_time = time.time()
                elif time.time() - answer_time > 3.5:
                    next_question()

        if not is_answered:
            try:
                line = ser.readline().decode('utf-8').strip()
                #double checking if line read is a INT
                if line.isdigit():
                    #REALLY MAKING SURE ITS A INT
                    y = int(line)
                    if y < 300 and y != 1:  # Up
                        highlight_index = (highlight_index - 1) % len(options)
                    elif y > 700:  # Down
                        highlight_index = (highlight_index + 1) % len(options)

                    elif y == 1:  # Answer submitted
                        selected_answer = chr(ord('A') + highlight_index)  # Convert index to letter
                        is_answered = True
                        showing_gif = True
                        if selected_answer == correct_answer:
                            score += 1

                    draw_buttons(options, highlight_index) #Highlight the selected answer
                    pygame.display.flip() #Update the display

            except serial.SerialException as e:
                print(f"Serial communication error: {e}")
                running = False
                break # Exit the loop on error to prevent further attempts

        display_text(f"Score: {score}", FONT, WHITE, WIDTH // 2, 20, center=True)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
if 'ser' in locals() and ser.is_open:
    ser.close()
sys.exit()