import pygame

from screeninfo import get_monitors

import random

from baum import *
from sprites import *

def initialize():
    pygame.init()
    pygame.font.init()
    res = []
    for m in get_monitors():
        res.append([m.width,m.height-60])
    screen = pygame.display.set_mode(res[0])
    return screen

def render_elements(display, text_eingabe:str, bild):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen_x, screen_y = display.get_width(), display.get_height()
    
    opt1 = Final()
    opt1.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    opt1.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    textxy = opt1.geben()[0].xy
    optsize = opt1.geben()[0].size
    textx = textxy[0] + (optsize[0]/2.5)
    texty = textxy[1] + (optsize[1]/3)
    opt1.hinzufuegen( Text(text="1", xy=[textx,texty]) )
    
    opt2 = Final()
    opt2.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.3, screen_y*0.8]) )
    opt2.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.3, screen_y*0.8]) )
    textxy = opt2.geben()[1].xy
    optsize = opt2.geben()[1].size
    textx = textxy[0] + (optsize[0]/2.5)
    texty = textxy[1] + (optsize[1]/3)
    opt2.hinzufuegen( Text(text="2", xy=[textx,texty]) )
    
    story = Final()
    story.hinzufuegen( Quadrat(color="white", size=[1000,750], xy=[screen_x*0.01, screen_y*0.01]) )
    story.hinzufuegen( Quadrat(rand=5, size=[1000,750], xy=[screen_x*0.01, screen_y*0.01]) )
    
    text = Final()
    text.hinzufuegen( Text(text=text_eingabe, wrap_to=story.geben()[0]) )
    #text.hinzufuegen( Text(text="Zum starten bitte eine beliebige Taste unten drücken (1 oder 2)", xy=[story.geben()[0].xy[0], story.geben()[0].xy[1]+15]) )
    
    sprlist = [opt1,opt2,story,text]
    for spr in sprlist:
        for obj in spr.geben():
            obj.malen(display)
    
    return sprlist
    
def get_all_sprites(sprite_list:list):
    final_list = []
    for s in sprite_list:
        final_list.append(s)
    return final_list

def render(display, gid:int):
    display.fill("gray")
    sprites = render_elements(display,"abc",None)
    pygame.display.flip()
    return sprites

def load(tree:Baum):
    screen = initialize()
    sprites = []
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = []
                for s in sprites:
                    for o in s.geben():
                        if (pos[0] > o.xy[0] and pos[1] > o.xy[1]) and (pos[0] < o.xy[0]+o.size[0] and pos[1] < o.xy[1]+o.size[1]):
                            clicked_sprites.append(o)
    
        sprites = get_all_sprites(render(screen, 0))
        clock.tick(60)

def main():
    load()

if __name__ == "__main__":
    main()
