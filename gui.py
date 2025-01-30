import pygame

from screeninfo import get_monitors

import random

from sprites import *

def initialize():
    pygame.init()
    pygame.font.init()
    res = []
    for m in get_monitors():
        res.append([m.width,m.height-60])
    screen = pygame.display.set_mode(res[0])
    return screen

def render_elements(display, text:str, bild):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen_x, screen_y = display.get_width(), display.get_height()
    
    opt1 = Final()
    opt1.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    opt1.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    
    opt2 = Final()
    opt1.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.3, screen_y*0.8]) )
    opt1.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.3, screen_y*0.8]) )
    
    story = Final()
    story.hinzufuegen( Quadrat(color="white", size=[1000,750], xy=[screen_x*0.01, screen_y*0.01]) )
    story.hinzufuegen( Quadrat(rand=5, size=[1000,750], xy=[screen_x*0.01, screen_y*0.01]) )
    
    sprlist = [opt1,opt2,story]
    for spr in sprlist:
        for obj in spr.geben():
            obj.malen(display)
    
    #text_surface = font.render(text, False, (0,0,0))
    #display.blit(text_surface, (60, 1))
    

def render(display, gid:int):
    display.fill("gray")
    render_elements(display,"Jony",None)
    pygame.display.flip()

def load():
    screen = initialize()
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
    
        render(screen, 0)
        clock.tick(60)

def main():
    load()

if __name__ == "__main__":
    main()
