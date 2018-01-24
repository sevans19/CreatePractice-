import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
is_blue = True
is_green = True
x = 30
y = 30
a = 100
b = 100

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_green = not is_green

    if pressed[pygame.K_w]: a -= 6
    if pressed[pygame.K_s]: a += 6
    if pressed[pygame.K_a]: b -= 6
    if pressed[pygame.K_d]: b += 6

    #screen.fill((0, 0, 0))
    if is_green:
        color2 = (0, 255, 0)
    else:
        color2 = (255, 51, 153)
    pygame.draw.rect(screen, color2, pygame.Rect(a, b, 100, 100))


    pygame.display.flip()
    clock.tick(60)