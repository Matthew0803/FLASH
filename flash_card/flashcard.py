import pygame
import sys
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multiple Choice Quiz Game")
quiz = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "correct": 2
    },
    {
        "question": "Which function is used to get user input in Python?",
        "choices": ["A. get()", "B. input()", "C. gets()", "D. scan()"],
        "correct": 1
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "choices": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "correct": 1
    }
]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
def render_text(text, x, y, color=BLACK):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))
def run_quiz():
    current_question = 0
    score = 0
    total_questions = len(quiz)

    while current_question < total_questions:
        question_data = quiz[current_question]
        question_text = question_data["question"]
        choices = question_data["choices"]
        correct_index = question_data["correct"]

        # Clear the screen
        screen.fill(WHITE)

        # Display the question
        render_text(question_text, 20, 50)

        # Display the choices
        for i, choice in enumerate(choices):
            render_text(choice, 20, 100 + i * 40)

        pygame.display.flip()

        # Wait for user input
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.:
                        selected = 0
                    elif event.key == pygame.K_b:
                        selected = 1
                    elif event.key == pygame.K_c:
                        selected = 2
                    elif event.key == pygame.K_d:
                        selected = 3
                    else:
                        continue

                    # Check if the selected answer is correct
                    if selected == correct_index:
                        score += 1

                    current_question += 1
                    waiting_for_input = False

    # Display final score
    screen.fill(WHITE)
    render_text(f"Your final score is {score} out of {total_questions}.", 20, 50)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_quiz()
