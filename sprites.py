
import pygame
from pygame import Rect, draw

class Sprite(object):
    def __init__(self, name:str="Object", rand:int=0, size:list=[10,10], xy:list=[0,0], color="black", *args, **kwargs):
        self.rand = rand
        self.size = size
        self.xy = xy
        self.color = color
        self.sprite = None
    
    def geben(self):
        return self.sprite

class Quadrat(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprite = Rect(self.xy[0], self.xy[1], self.size[0], self.size[1])
    
    def malen(self, display):
        draw.rect(display, self.color, self.sprite, width=self.rand)

class Text(Sprite):
    def __init__(self, text:str="Beispieltext", font:str="Comic Sans MS", text_size:int=15,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.font = font
        self.text_size = text_size

        sysfont = pygame.font.SysFont(self.font, self.text_size)
        self.sprite = sysfont.render(text, False, (0,0,0))
    
    def malen(self, display):
        display.blit(self.sprite, (self.xy[0]+5,self.xy[1]+5))

class Final(object):
    def __init__(self, name:str="Sprite"):
        self.liste = []
    
    def geben(self):
        return self.liste
    
    def hinzufuegen(self, objekt:Sprite, pos:int=0):
        if pos <= 0:
            self.liste.append(objekt)
        else:
            self.liste.insert(pos-1, objekt)

def main():
    return

if __name__ == "__main__":
    main()
