import pygame
pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hello world!")

x = 560
y = 500
width = 40
height = 60
vel = 10

run = True
while run:
    pygame.time.delay(50)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x>0:
            x -= vel   
    if keys[pygame.K_RIGHT]:
        if x<560:
            x += vel
    if keys[pygame.K_UP]:
        if y>0:
            y -= vel
    if keys[pygame.K_DOWN]:
        if y<540:
            y += vel
    
    
    window.fill((0, 0, 0))
    rect = pygame.draw.rect(window, (211, 219, 84), (x, y, width, height))

    

    pygame.display.update()

pygame.quit()