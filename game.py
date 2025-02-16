import pygame
import os

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
WIDTH, HEIGHT = 600, 800  # More vertical screen
FPS = 10  # Adjusted for smooth GIF animation
FONT = pygame.font.Font(None, 36)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flashcard Game")

# Create a clock to control frame rate
clock = pygame.time.Clock()

# Define flashcards (question, answer choices, correct answer)
flashcards = [
    ("What is 2 + 2?", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
    ("What is the capital of France?", ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "C"),
    ("What is 5 * 5?", ["A) 20", "B) 25", "C) 30", "D) 35"], "B"),
]

# Game Variables
score = 0
question_index = 0
selected_answer = None
is_answered = False
is_game_over = False
showing_gif = False
gif_index = 0

# Load GIF frames
def load_gif(folder):
    """Load frames from a folder and return as a list"""
    frames = []
    for filename in sorted(os.listdir(folder)):  # Ensure frames are loaded in order
        if filename.endswith(".png"):  # Convert GIF to PNG sequence first
            frame = pygame.image.load(os.path.join(folder, filename))
            frames.append(frame)
    return frames

# Load correct/incorrect GIF frames (Ensure they are extracted as PNG sequence)
correct_frames = load_gif("correct_gif")  # Folder should contain frame1.png, frame2.png, etc.
incorrect_frames = load_gif("incorrect_gif")  # Folder should contain frame1.png, frame2.png, etc.

# Function to display text
def display_text(text, font, color, x, y):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Function to draw answer buttons (lowered on the screen)
def draw_buttons(options, highlight_index=None):
    button_height = 50  # Height of the answer boxes
    button_width = 500
    y_offset = 550  # Lowered position
    radius = 20  # Rounded corners

    for idx, option in enumerate(options):
        color = BLUE
        if idx == highlight_index:
            color = GREEN  # Highlight correct selection
        pygame.draw.rect(screen, color, (50, y_offset + idx * (button_height + 10), button_width, button_height), border_radius=radius)
        display_text(option, FONT, WHITE, 75, y_offset + idx * (button_height + 10) + 10)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if is_game_over:
        display_text(f"Game Over! Final Score: {score}", FONT, YELLOW, 150, 180)

    else:
        question, options, correct_answer = flashcards[question_index]

        # Display question
        display_text(question, FONT, YELLOW, 50, 50)

        if not is_answered:
            draw_buttons(options)

        else:
            # Play GIF animation
            if showing_gif:
                if gif_index < len(correct_frames):  # Keep playing GIF frames
                    if selected_answer == correct_answer:
                        screen.blit(correct_frames[gif_index], (150, 250))  # Adjust position
                    else:
                        screen.blit(incorrect_frames[gif_index], (150, 250))

                    gif_index += 1  # Move to the next frame
                else:
                    # GIF finished playing, move to the next question
                    showing_gif = False
                    gif_index = 0

                    question_index += 1
                    if question_index >= len(flashcards):  # End the game if all questions are asked
                        is_game_over = True
                    else:
                        is_answered = False
                        selected_answer = None

        # Handle input
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

        # Display score
        display_text(f"Score: {score}", FONT, WHITE, 250, 20)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
