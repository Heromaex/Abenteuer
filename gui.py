import pygame
from pygame import Rect,draw

from screeninfo import get_monitors

import random

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
    
    opt1 = Rect(1,1,10,10)
    opt2 = Rect(10,1,50,500)
    story = Rect(60,1,500,500)
    text_surface = font.render(text, False, (0,0,0))

    draw.rect(display, "black", opt1)
    draw.rect(display, "black", opt2)
    draw.rect(display, "gray", story)
    display.blit(text_surface, (60, 1))
    

def render(display, gid:int):
    display.fill("white")
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
