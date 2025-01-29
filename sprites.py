
import pygame

def Sprite(object):
    def __init__(self, fill:bool=True *args, **kwargs):
        self.fill = fill

def Quadrat(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.sprite = Rect()

def Text(Sprite):
    def __init__(self, font:str="Comic Sans MS", text_size:int=15,  *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
        self.font = font
        self.text_size = text_size

        sysfont = pygame.font.SysFont(self.font, self.text_size)
        self.sprite = sysfont.render
        
def main():
    return

if __name__ == "__main__":
    main()
