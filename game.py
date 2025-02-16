import pygame
import os
import time
import json

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
    global question_index, is_answered, selected_answer, showing_gif, gif_index, is_game_over, answer_time
    
    question_index += 1
    if question_index >= len(flashcards):
        is_game_over = True
    else:
        is_answered = False
        selected_answer = None
        showing_gif = False
        gif_index = 0
        answer_time = None

# Main loop
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
            draw_buttons(options)

        else:
            if showing_gif:
                if gif_index < len(correct_frames):  
                    frame = correct_frames[gif_index] if selected_answer == correct_answer else incorrect_frames[gif_index]
                    screen.blit(frame, frame.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
                    gif_index += 1  

                if selected_answer == correct_answer:
                    display_text("Correct!", FONT, GREEN, WIDTH // 2, HEIGHT // 2 + 120, center=True)
                else:
                    display_text("Incorrect!", FONT, RED, WIDTH // 2, HEIGHT // 2 + 100, center=True)

                display_text(f"Correct Answer: {correct_answer}", FONT, YELLOW, WIDTH // 2, HEIGHT // 2 + 140, center=True)


                if answer_time is None:
                    answer_time = time.time()
                elif time.time() - answer_time > 4:
                    next_question()

        if not is_answered:
            keys = pygame.key.get_pressed()
            highlight_index = None

            if keys[pygame.K_a]:
                selected_answer = "A"
                is_answered = True
                showing_gif = True
                highlight_index = 0
                if selected_answer == correct_answer:
                    score += 1
            elif keys[pygame.K_b]:
                selected_answer = "B"
                is_answered = True
                showing_gif = True
                highlight_index = 1
                if selected_answer == correct_answer:
                    score += 1
            elif keys[pygame.K_c]:
                selected_answer = "C"
                is_answered = True
                showing_gif = True
                highlight_index = 2
                if selected_answer == correct_answer:
                    score += 1
            elif keys[pygame.K_d]:
                selected_answer = "D"
                is_answered = True
                showing_gif = True
                highlight_index = 3
                if selected_answer == correct_answer:
                    score += 1

            draw_buttons(options, highlight_index)

        display_text(f"Score: {score}", FONT, WHITE, WIDTH // 2, 20, center=True)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
