import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Cath")

# Load and resize the first image with alpha channel
IMAGE = pygame.image.load("sprite1.png").convert_alpha()
IMAGE = pygame.transform.scale(IMAGE, (50, 50))  # Resize to 50x50 pixels

# Load and resize the second image with alpha channel
IMAGE2 = pygame.image.load("sprite2.png").convert_alpha()
IMAGE2 = pygame.transform.scale(IMAGE2, (50, 50))  # Resize to 50x50 pixels

# Load the background image
background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))

# Create a rect for the first image
rect = IMAGE.get_rect()
rect.center = (10, 10)

# Create a rect for the second image
rect2 = IMAGE2.get_rect()
rect2.center = (20, 20)  # Adjust the initial position as needed

# Create a clock object to control FPS
clock = pygame.time.Clock()
desired_fps = 60  # Set your desired FPS here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Check for key presses
    if keys[pygame.K_LEFT]:
        rect.move_ip(-2, 0)
    if keys[pygame.K_RIGHT]:
        rect.move_ip(2, 0)
    if keys[pygame.K_UP]:
        rect.move_ip(0, -2)
    if keys[pygame.K_DOWN]:
        rect.move_ip(0, 2)

    # Check for key presses for the second image
    if keys[pygame.K_a]:
        rect2.move_ip(-2, 0)  # Move left
    if keys[pygame.K_d]:
        rect2.move_ip(2, 0)   # Move right
    if keys[pygame.K_w]:
        rect2.move_ip(0, -2)  # Move up
    if keys[pygame.K_s]:
        rect2.move_ip(0, 2)   # Move down

    # Blit the background first
    window.blit(background, (0, 0))
    window.blit(IMAGE, rect)
    window.blit(IMAGE2, rect2)  # Blit the second image

    pygame.display.update()

    # Limit the frame rate to the desired FPS
    clock.tick(desired_fps)