import random
import json

# Klasse Datenelement um Daten in einem Knoten zu speichern
class Datenelement(object):
    def __init__(self):
        return
    
    def info_geben(self):
        return self.story
    
    def titel_holen(self, *args):
        return None
    
    def istGleich(self, vgl):
        return self.titel == vgl
    
    def istGroesser(self, vgl):
        return len(self.titel) > len(vgl)

# Datelement Raum
# Diese Klasse speichert die ID des Raums um spezifische Methoden zu unterstützen
# Sie enthält auch den Titel und die Geschichte
class Raum(Datenelement):
    def __init__(self, story:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rid = random.randint(1000000,9999999)
        self.story = story
        self.titel = self.titel_holen()
    
    def titel_holen(self, datei:str="raeume.json"):
        with open(datei, "r") as f:
            con = json.load(f)
        return con[self.story][0]
    
    def geschichte_holen(self, datei:str="raeume.json"):
        with open(datei, "r") as f:
            con = json.load(f)
        return con[self.story][1]
    
    def weiter(self):
        return 1

class Ende(Datenelement):
    def __init__(self, story:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.story = story
        self.titel = "Ende"
    
    def geschichte_holen(self, datei:str="enden.json"):
        with open(datei, "r") as f:
            con = json.load(f)
        return con[self.story][1]
    
    def weiter(self):
        return 0

def main():
    return

if __name__ == "__main__":
    main()
