from datenelement import *
from baumelement import *
from baum import *
from gui import *

import pygame

# Vorgefertigter Binärbaum, der für Tests und als Beispielspiel dient
class Adventure():
    spiel = Baum()
    
    neud = Datenelement("Wald", 1)
    neu1 = Knoten(neud)
    
    neud = Datenelement("Dorf", 2)
    neu2 = Knoten(neud)

    def start():
        load()

def main():
    a = Adventure()
    load()

if __name__ == "__main__":
    main()
