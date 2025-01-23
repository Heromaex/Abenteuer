import random

# Klasse Datenelement um Daten in einem Knoten zu speichern
class Datenelement(object):
    def __init__(self):
        return

# Datelement Raum
# Diese Klasse speichert die ID des Raums um spezifische Methoden zu unterstützen
# Sie enthält auch den Titel und die Geschichte
class Raum(Datenelement):
    def __init__(self, titel:str, story:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rid = random.randint(1000000,9999999)
        self.titel = titel
        self.story = story

def main():
    return

if __name__ == "__main__":
    main()
