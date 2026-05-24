import pygame

pygame.init()

window=pygame.display.set_mode((400,400))
window.fill((255,255,255))
BLACK=((0,0,0))

pygame.draw.circle(window, BLACK,(300,300), 50)
pygame.draw.circle(window,BLACK,(100,100),50, 5)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    pygame.display.flip()

