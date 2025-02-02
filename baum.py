from baumelement import *
from datenelement import *

# Klasse Baum die alle Elemente verwaltet und trägt
class Baum(object):
    def __init__(self):
        # Der Anfang wird gesetzt um ein Klares Ende zu haben
        # Für jedes Blatt wird ein/zwei neuer Abschluss eingesetzt
        self.anfang = Abschluss()

    # Suche nach einem spezifischen Element des Baums
    # suchen_id() sucht den Knoten mit seiner ID
    # suchen_name() sucht den Knoten mit seinem Namen
    def suchen(self, rid:int):
        # Rekursionsanfang
        ergebnis = self.anfang.suchen(rid)
        return ergebnis
    
    def einfuegen(self, raum:Baumelement, nach_name:str, rl:int):
        self.anfang.einfuegen(raum, nach_name, rl)
    
    def wurzel_setzen(self, raum:Baumelement):
        self.anfang = raum
    
    # Fügt ein Element nach ID sortiert in den Baum ein
    def sortiert_einfuegen(self, element:Baumelement):
        self.anfang.sortiert_einfuegen_id(element)

def main():
    return

if __name__ == "__main__":
    main()
