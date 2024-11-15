import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Rectangle")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Rectangle properties
rect_x, rect_y = 200, 150
rect_width, rect_height = 50, 30
speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Fill the screen and draw the rectangle
    screen.fill(white)
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()

pygame.quit()
