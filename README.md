# phe-compare
Dieses Repository enthält die Implementationen, Tests und Analyseergebnisse der Masterarbeit "Kryptologische Tools - ein Vergleich von Realisierungen partiell
homomorpher Verschlüsselungen".\
Die meisten Verschlüsselungen und die grundlegende Struktur stammen aus [LightPHE](https://github.com/serengil/LightPHE).\
Weitere verwendeten Algorithmen basieren auf Implementationen der folgenden Bibliotheken:

DGK: [TNO PET Lab](https://github.com/TNO-MPC)\
ASHE: [Cuttlefish](https://github.com/ssavvides/cuttlefish)\
SAHE/SMHE: [symmetria](https://github.com/ssavvides/symmetria)

Struktur:
------
/lightphe: enthält die Algorithmen (nicht nur die von LightPHE übernommenen/bearbeiteten)\
/pickle...: enthalten .pickle Instanzen von Listen oder einzelnen Schlüsseltexten der entsprechenden Algorithmen. Die Parameter sind im Namen der jeweiligen .pickle Datei.\
Die .pickle Dateien sind Instanzen von Kryptosystemen.\
[Algorithmus]G.py sind Klassen zum direkten aufrufen der Operationen der entsprechenden Verschlüsselung. \
Test....py sind die Klassen, die die Tests enthalten, die mit den Python-Paketen pyperf (Zeiteffizienz) bzw. tracmalloc (Speichereffizienz) funktionieren. Teilweise sind diese nicht mehr vollständig/auskommentiert, wenn die Tests für ein Teil der Parameter wiederholt werden mussten.\
....json Dateien enthalten die verschiedenen Testergebnisse. Nicht alle davon sind Teil der finalen Arbeit.
