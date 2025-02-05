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

def render_elements(display, titel:str, text_eingabe:str, bild, right_screen:str=""):
    screen_x, screen_y = display.get_width(), display.get_height()
    
    opt1 = Final(name="links")
    opt1.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.2, screen_y*0.85]) )
    opt1.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.2, screen_y*0.85]) )
    textxy = opt1.geben()[0].xy
    optsize = opt1.geben()[0].size
    textx = textxy[0] + (optsize[0]/2.5)
    texty = textxy[1] + (optsize[1]/3)
    opt1.hinzufuegen( Text(text="1", xy=[textx,texty]) )
    
    opt2 = Final(name="rechts")
    opt2.hinzufuegen( Quadrat(color="white", size=[100,75], xy=[screen_x*0.3, screen_y*0.85]) )
    opt2.hinzufuegen( Quadrat(rand=5, size=[100,75], xy=[screen_x*0.3, screen_y*0.85]) )
    textxy = opt2.geben()[1].xy
    optsize = opt2.geben()[1].size
    textx = textxy[0] + (optsize[0]/2.5)
    texty = textxy[1] + (optsize[1]/3)
    opt2.hinzufuegen( Text(text="2", xy=[textx,texty]) )
    
    story = Final()
    story.hinzufuegen( Quadrat(color="white", size=[1000,750], xy=[screen_x*0.01, screen_y*0.05]) )
    story.hinzufuegen( Quadrat(rand=5, size=[1000,750], xy=[screen_x*0.01, screen_y*0.05]) )
    
    story_titel = Final()
    story_titel_xy = story.geben()[0].xy
    story_titel.hinzufuegen( Text(text=titel, xy=[story_titel_xy[0],story_titel_xy[1]-30]) )
    
    text = Final()
    text.hinzufuegen( Text(text=text_eingabe, wrap_to=story.geben()[0]) )
    
    settings = Final(name="settings")
    settings.hinzufuegen( Quadrat(color="white", size=[150,30], xy=[1050+screen_x*0.01,screen_y*0.05]) )
    settings.hinzufuegen( Text(text="Einstellungen", xy=[1050+screen_x*0.01,screen_y*0.05]) )
    
    reset = Final(name="reset")
    reset.hinzufuegen( Quadrat(color="white", size=[150,30], xy=[1050+screen_x*0.01,35+screen_y*0.05]) )
    reset.hinzufuegen( Text(text="Zurücksetzen", xy=[1050+screen_x*0.01,35+screen_y*0.05]) )
    
    inventar = Final(name="inventory")
    inventar.hinzufuegen( Quadrat(color="white", size=[150,30], xy=[1050+screen_x*0.01,70+screen_y*0.05]) )
    inventar.hinzufuegen( Text(text="Inventar", xy=[1050+screen_x*0.01,70+screen_y*0.05]) )
    
    stats = Final(name="stats")
    stats.hinzufuegen( Quadrat(color="white", size=[150,30], xy=[1050+screen_x*0.01,105+screen_y*0.05]) )
    stats.hinzufuegen( Text(text="Statistik", xy=[1050+screen_x*0.01,105+screen_y*0.05]) )
    
    sidemenu = Final(name="sidemenu")
    sidemenu.hinzufuegen( Quadrat(color="white", size=[500,750], xy=[1250+screen_x*0.01, screen_y*0.05]) )
    sidemenu.hinzufuegen( Quadrat(rand=5, size=[500,750], xy=[1250+screen_x*0.01, screen_y*0.05]) )
    sidemenu.hinzufuegen( Text(text=right_screen, wrap_to=sidemenu.geben()[0]) )
    
    sprlist = [opt1,opt2,story,story_titel,text,settings,reset,inventar,stats,sidemenu]
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
    sprites = render_elements(display,format_char(get_items(rid)[0]),format_char(get_items(rid)[1]),None)
    pygame.display.flip()
    return sprites

def is_clicked(sprites:list, name:str):
    for s in sprites:
        if s.name_holen() == name:
            return True
    return False

def check_right_screen(sprites:list):
    for s in ["settings", "reset", "inventory", "stats", "sidemenu"]:
        if is_clicked(sprites, s):
            return s
    return None

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
    right_screen = ""
    right_screen_titel = ""
    
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
                
                with open("right_screen.json", "r") as f:
                    con = json.load(f)
                checked_sprite = check_right_screen(clicked_sprites)
                if checked_sprite:
                    right_screen_titel = con[checked_sprite][0]
                    right_screen = con[checked_sprite][1]
        
        if not current.typ:
            render(screen, "--")
            running = False
            break
        
        sprites = get_all_sprites(render(screen, current.daten.story, right_screen=right_screen))
        if not current.daten.weiter():
            running = False
        
        clock.tick(60)
    
    running = True
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

def main():
    load()

if __name__ == "__main__":
    main()
