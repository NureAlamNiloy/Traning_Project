import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GROUND_HEIGHT = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_width = 50
player_height = 50
player_x = WIDTH // 4
player_y = HEIGHT - GROUND_HEIGHT - player_height
player_speed = 7
jump_height = 15
gravity = 1

# Obstacle
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Run Game")

# Load images
player_image = pygame.Surface((player_width, player_height))
player_image.fill(RED)

obstacle_image = pygame.Surface((obstacle_width, obstacle_height))
obstacle_image.fill(RED)

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_ground():
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

def draw_player(x, y):
    screen.blit(player_image, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_image, (x, y))

def main():
    global player_y, player_speed, gravity

    obstacle_x = WIDTH
    obstacle_y = HEIGHT - GROUND_HEIGHT - obstacle_height

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_y == HEIGHT - GROUND_HEIGHT - player_height:
            gravity = -jump_height

        player_y += gravity
        gravity += 1

        obstacle_x -= obstacle_speed
        if obstacle_x < 0:
            obstacle_x = WIDTH
            obstacle_y = HEIGHT - GROUND_HEIGHT - obstacle_height

        # Collision detection
        if (
            player_x < obstacle_x + obstacle_width
            and player_x + player_width > obstacle_x
            and player_y < obstacle_y + obstacle_height
            and player_y + player_height > obstacle_y
        ):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        # Draw everything
        screen.fill((0, 0, 0))
        draw_ground()
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        pygame.display.flip()

        # Set the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
