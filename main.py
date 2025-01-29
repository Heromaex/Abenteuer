from datenelement import *
from baumelement import *
from baum import *
from gui import *

import pygame

# Vorgefertigter Binärbaum, der für Tests und als Beispielspiel dient
class Adventure():
    spiel = Baum()

    def start():
        load()

def main():
    a = Adventure()
    load()

if __name__ == "__main__":
    main()
