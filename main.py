from datenelement import *
from baumelement import *
from baum import *
from gui import *

import pygame

# Vorgefertigter Binärbaum, der für Tests und als Beispielspiel dient
class Adventure():
    spiel = Baum()
    
    neud = Raum("Wald", 1)
    neu1 = Knoten(neud)
    
    neud = Raum("Dorf", 2)
    neu2 = Knoten(neud)

    neud = Raum("", 3)

    def start():
        load()

def main():
    a = Adventure()
    load()

if __name__ == "__main__":
    main()
