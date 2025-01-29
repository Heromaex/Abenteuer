from datenelement import *

# Klasse Baumelement zum initialisieren der Klassen Knoten und Abschluss
class Baumelement(object):
    def __init__(self, *args, **kwargs):
        return

# Baumelement Knoten, Element des Baums der Daten speichert
class Knoten(Baumelement):
    def __init__(self, daten:Datenelement, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.linker_nachfolger = Abschluss()
        self.rechter_nachfolger = Abschluss()
        self.daten = daten

    # Methode suchen() gibt den gesuchten Knoten zurück
    # Wenn dieser Knoten die selbe ID hat, gibt er sich selbst zurück
    # Ansonten ruft er die Methode bei den Nachfolgern auf
    def suchen(self, rid:int):
        # Prüfen ob dieser Knoten gesucht wird
        if daten.id == rid:
            return self
        # Ruft korrektes Nachfolger-Element auf zum weitersuchen
        elif rid < daten.id:
            return linker_nachfolger.suchen(rid)
        return rechter_nachfolger.suchen(rid)

    # Fügt den gegebenen Knoten korrekt ein
    # Gibt das gegebene Element an den Nachfolger weiter
    def sortiert_einfuegen(self, element:Baumelement):
        # Sollte dieser Knoten die selbe ID haben, hat man Pech
        if element.id_geben() == daten.id:
            raise ValueError("Duplikat der ID gefunden, herzlichen Glückwunsch Sie haben Ihre Chance im Lotto zu gewinnen gerade verloren")
        # Weitergeben
        elif element.id_geben() < daten.id:
            linker_nachfolger = linker_nachfolger.sortiert_einfuegen(element)
        rechter_nachfolger = rechter_nachfolger.sortiert_einfuegen(element)
        return self

    # Gibt die eigene ID aus
    def id_geben(self):
        return daten.rid

# Baumelement Abschluss, vollendet jeden Pfad des Baumes und ist Nachfolger eines Blattes
class Abschluss(Baumelement):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    # Fügt das Element an dieser Position ein
    def sortiert_einfuegen(self, element:Baumelement):
        return element

    # Gibt zurück, dass der Knoten nicht gefunden wurde
    def suchen(self, rid):
        return None

def main():
    return

if __name__ == "__main__":
    main()
