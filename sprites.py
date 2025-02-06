
import pygame
from pygame import Rect, draw

class Sprite(object):
    def __init__(self, name:str="Object", rand:int=0, size:list=[10,10], xy:list=[0,0], color="black", *args, **kwargs):
        self.name = name
        self.rand = rand
        self.size = size
        self.xy = xy
        self.color = color
        self.sprite = None
    
    def geben(self):
        return self.sprite
    
    def name_holen(self):
        return self.name

class Quadrat(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprite = Rect(self.xy[0], self.xy[1], self.size[0], self.size[1])
    
    def malen(self, display):
        draw.rect(display, self.color, self.sprite, width=self.rand)

class Text(Sprite):
    def __init__(self, text:str="Beispieltext", font:str="Comic Sans MS", text_size:int=15, wrap_to:Rect=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.text = text
        self.font = font
        self.text_size = text_size

        self.sysfont = pygame.font.SysFont(self.font, self.text_size)
        self.wrap_to = wrap_to
        self.sprite = self.sysfont.render(text, True, (0,0,0))
    
    def malen(self, display):
        if self.wrap_to == None:
            display.blit(self.sprite, (self.xy[0]+5, self.xy[1]+5))
            return self.text
        else:
            rect = Rect(self.wrap_to.sprite)
            y = rect.top + 5
            lineSpacing = -2
            fontHeight = self.sysfont.size("Tg")[1]
            
            while self.text:
                i = 1
                
                if (y + fontHeight) > rect.bottom:
                    break
                while self.sysfont.size(self.text[:i])[0] < rect.width-20 and i < len(self.text):
                    i += 1
                if i < len(self.text):
                    i = self.text.rfind(" ", 0, i) + 1
                
                image = self.sysfont.render(self.text[:i], True, self.color)
                display.blit(image, (rect.left+10, y))
                
                y += fontHeight + lineSpacing
                self.text = self.text[i:]
            return self.text

class Final(object):
    def __init__(self, name:str="Sprite"):
        self.name = name
        self.liste = []
    
    def geben(self):
        return self.liste
    
    def hinzufuegen(self, objekt:Sprite, pos:int=0):
        if pos <= 0:
            self.liste.append(objekt)
        else:
            self.liste.insert(pos-1, objekt)
    
    def name_holen(self):
        return self.name

def main():
    return

if __name__ == "__main__":
    main()
