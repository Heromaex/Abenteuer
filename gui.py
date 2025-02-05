import pygame

from screeninfo import get_monitors

import random
import json
import sys

from baum import *
from sprites import *

def exit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def render_elements(display, text_eingabe:str, bild):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen_x, screen_y = display.get_width(), display.get_height()
    
    opt1 = Final(name="links")
    opt1.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    opt1.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.2, screen_y*0.8]) )
    textxy = opt1.geben()[0].xy
    optsize = opt1.geben()[0].size
    textx = textxy[0] + (optsize[0]/2.5)
    texty = textxy[1] + (optsize[1]/3)
    opt1.hinzufuegen( Text(text="1", xy=[textx,texty]) )
    
    opt2 = Final(name="rechts")
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
    
    sprlist = [opt1,opt2,story,text]
    for spr in sprlist:
        for obj in spr.geben():
            obj.malen(display)
    
    return sprlist

def initialize():
    pygame.init()
    pygame.font.init()
    res = []
    for m in get_monitors():
        res.append([m.width,m.height-60])
    screen = pygame.display.set_mode(res[0])
    
    return screen

def get_items(rid:str):
    with open("raeume.json", "r") as f:
        con = json.load(f)
    ergebnis = con[rid]
    return ergebnis

def get_all_sprites(sprite_list:list):
    final_list = []
    for s in sprite_list:
        final_list.append(s)
    return final_list

def format_char(text:str):
    x = text.replace("Ã¤","ae").replace("Ã¶","oe").replace("Ã¼","ue").replace("ÃŸ","ss")
    return x

def render(display, rid:str):
    display.fill("gray")
    sprites = render_elements(display,format_char(get_items(rid)[1]),None)
    pygame.display.flip()
    return sprites

def is_clicked(sprites:list, name:str):
    for s in sprites:
        if s.name_holen() == name:
            return True
    return False

def load(tree:Baum):
    screen = initialize()
    sprites = render(screen, "++")
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                running = False
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clicked_sprites = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for s in sprites:
                    for o in s.geben():
                        if (pos[0] > o.xy[0] and pos[1] > o.xy[1]) and (pos[0] < o.xy[0]+o.size[0] and pos[1] < o.xy[1]+o.size[1]):
                            clicked_sprites.append(s)
                            break
                
                if is_clicked(clicked_sprites, "links") or is_clicked(clicked_sprites, "rechts"):
                    running = False
        sprites = render(screen, "0")
    
    running = True
    current = tree.spiel.starten()
    
    while running:
        clicked_sprites = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for s in sprites:
                    for o in s.geben():
                        if (pos[0] > o.xy[0] and pos[1] > o.xy[1]) and (pos[0] < o.xy[0]+o.size[0] and pos[1] < o.xy[1]+o.size[1]):
                            clicked_sprites.append(s)
                
                if is_clicked(clicked_sprites, "links"):
                    current = current.links_geben()
                elif is_clicked(clicked_sprites, "rechts"):
                    current = current.rechts_geben()
        
        if not current.typ:
            render(screen, "--")
            running = False
            break
        
        sprites = get_all_sprites(render(screen, current.daten.story))
        if not current.daten.weiter():
            running = False
        clock.tick(60)

def main():
    load()

if __name__ == "__main__":
    main()
