import random

class Entity(object):
    def __init__(self):
        return
    
    def kampfkraft_berechnen(self):
        augenzahl = random.randint(2,12)
        return augenzahl + self.gewandtheit
    
    def kampfkraft_vergleichen(self, gegner):
        eigenkraft = self.kampfkraft_berechnen()
        gegnerkraft = enemy.kampfkraft_berechnen()
        if eigenkraft == gegnerkraft:
            return None
        return eigenkraft > gegnerkraft
    
    def schaden(self, anzahl:int):
        self.staerke -= anzahl

class Spieler(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.start_gewandtheit = 6 + random.randint(1,6)
        self.start_staerke = 12 + random.randint(2,12)
        self.start_glueck = 6 + random.randint(1,6)
        
        self.gewandtheit = self.start_gewandtheit
        self.staerke = self.start_staerke
        self.glueck = self.start_glueck
        
        self.rucksack = []
        self.gold = 0
        self.edelsteine = 0
        self.zaubertraenke = 0
        self.proviant = []
    
    def angreifen(self, gegner:Entity):
        ergebnis = kampfkraft_vergleichen(gegner)
        if ergebnis[0] == None:
            return
        if ergebnis[0]:
            gegner.schaden(2)
        else:
            self.schaden(2)

class Gegner(Entity):
    def __init__(self, name:str, gewandtheit:int, staerke:int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.name = name
        self.gewandtheit = gewandtheit
        self.staerke = staerke

def main():
    return

if __name__ == "__main__":
    main()