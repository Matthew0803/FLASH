import pygame
import serial
import time

# Initialize Pygame
pygame.init()

# Set up serial communication (replace 'COM3' with your Arduino's port)
ser = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for the serial connection to initialize

# Pygame screen setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Joystick Navigation")

# Options and selection
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_option = 0

# Function to render options
def render_options():
    screen.fill((0, 0, 0))  # Clear screen
    font = pygame.font.Font(None, 36)
    for i, option in enumerate(options):
        color = (255, 0, 0) if i == selected_option else (255, 255, 255)
        text = font.render(option, True, color)
        screen.blit(text, (100, 100 + i * 40))
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ser.in_waiting > 0:
        command = ser.readline().decode().strip()
        if command == "UP":
            selected_option = (selected_option - 1) % len(options)
        elif command == "DOWN":
            selected_option = (selected_option + 1) % len(options)
        elif command == "SELECT":
            print(f"Selected: {options[selected_option]}")
            # Add your code here to handle the selected option

    render_options()
    pygame.time.wait(100)  # Adjust as needed

# Clean up
ser.close()
pygame.quit()
