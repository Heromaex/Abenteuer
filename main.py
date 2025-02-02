from datenelement import *
from baumelement import *
from baum import *
from gui import *
from entities import *

import pygame

# Vorgefertigter Binärbaum, der für Tests und als Beispielspiel dient
class Adventure():
    spiel = Baum()
    spieler = Spieler()
    
    neud = Raum(1)
    wurzel = Knoten(neud)
    
    neud = Raum(71)
    neu1 = Knoten(neud)

    neud = Raum(278)
    neu2 = Knoten(neud)
    
    spiel.wurzel_setzen(wurzel)
    spiel.einfuegen(neu1, "1", 0)
    spiel.einfuegen(neu2, "1", 1)

    def start():
        load()

def main():
    a = Adventure()
    load()

if __name__ == "__main__":
    main()
