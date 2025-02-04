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
    
    neud = Raum("1")
    wurzel = Knoten(neud)
    spiel.wurzel_setzen(wurzel)

    neud = Raum("71")
    neu = Knoten(neud)
    spiel.einfuegen(neu, "1", 0)

    neud = Raum("278")
    neu = Knoten(neud)
    spiel.einfuegen(neu, "1", 0)

    def start():
        load(self)

def main():
    a = Adventure()
    a.start()

if __name__ == "__main__":
    main()
