import pygame

# text_object_function
def text_object(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def event_message(s,msg):
    myfont = pygame.font.Font("font/kahlil-font/Kahlil-YzP9L.ttf", int(s.height/6))
    game_over = myfont.render(msg, 1, (0,0,0))
    dim = game_over.get_size()
    s.screen.blit(game_over, (int((s.width-dim[0])/2),int((s.height-dim[1])/2)))
    pygame.display.update()

def quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        sys.exit()