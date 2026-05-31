import pygame

pygame.init()

SCREEN_WIDTH,SCREEN_HEIGHT= 640,480 

display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Creating realistic scenes')
display_surface.fill((255,255,255))

trophy_image=pygame.transform.scale(
    pygame.image.load('Champions_League_Trophy.jpg').convert_alpha(),(300,300))
trophy_rect=trophy_image.get_rect(center=(SCREEN_WIDTH//2,
                                  SCREEN_HEIGHT//2 -30))

text=pygame.font.Font(None,20).render('1976-77, 1977-78, 1980-81, 1983-84, 2004-5, 20018-19 --> Liverpool fc',True,pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+ 110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running: 
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
               running=False

        
        display_surface.blit(trophy_image, trophy_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        pygame.display.set_caption('My first Project')

        clock.tick(10)

    pygame.quit()

if __name__== '__main__':
    game_loop()


  

