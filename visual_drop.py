import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Setup the Screen Dimensions (Width, Height in pixels)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My O-Level Physics Engine")

# Our Ball Properties
ball_x = 400  # Right in the middle of our 800-pixel width
ball_y = 50   # Near the top of our 600-pixel height
ball_radius = 20  # Size of the ball in pixels
ball_velocity_y = 0


# 3. The Main Game Loop (Keeps the window open)
running = True
while running:
    # Check if user clicked the 'X' button to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with a clean white color (RGB values)
    screen.fill((255, 255, 255))

     # Draw a blue ball on the screen
    pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), ball_radius)
    ball_y += ball_velocity_y
    ball_velocity_y += 0.1
    # Update the visual display
    pygame.display.flip()

# Clean up and close
pygame.quit()
sys.exit()
