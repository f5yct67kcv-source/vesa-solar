# vesa-solar.ch

Neuer Auftritt für die **VeSa Solar GmbH**, Rütiweg 6, 5706 Boniswil AG.
Photovoltaik-Montage vom Einfamilienhaus bis zur Halle. Gestaltung und Umsetzung:
formateins (Adrian von Arb).

Die heutige Seite läuft im Hostpoint-Baukasten. Dieses Repository löst sie ab.

## Stand

Entwurfsphase. Noch nichts ist live, es gibt keinen Deploy.

| Ordner, Datei | Inhalt |
|---|---|
| `IDEEN.md` | Analyse der heutigen Seite, Konkurrenz, Idee «Die Monteure», Bausteine |
| `entwuerfe/` | Startseiten-Entwürfe als reines HTML, `index.html` listet sie |
| `entwuerfe/bilder/` | Renderings der Entwürfe, Desktop und Handy |
| `fotos/` | Fotos und Logo von der heutigen Seite, als WebP verkleinert |
| `LOGBUCH.md` | Entscheide und offene Punkte, Nummern VES-… |
| `CLAUDE.md` | Arbeitsweise in diesem Repository |

## Entwürfe ansehen

Lokal:

```
python3 -m http.server 8000
```

Dann `http://localhost:8000/entwuerfe/` öffnen. Die Dach-Abfrage in Entwurf E
fragt die Schnittstelle des Bundes direkt aus dem Browser ab und braucht Netz.

## Gestaltung, wie entschieden

- **Farben nur aus dem Logo.** Schwarz, `#181818`, `#484848`, `#808080`,
  `#989898`, `#b0b0b0`, `#c8c8c8`, Weiss. Keine Akzentfarbe. Farbe kommt aus
  den Fotos.
- **Hell und dunkel**, mit Schalter im Kopf.
- **Zahlen** tragen die Seite: Zähler, Datenblätter pro Dach.
- **Technik zeigen**: Dach-Abfrage beim Bund (Sonnendach, BFE), Live-Tafel mit
  Sonnenstand, Montagesystem Schicht für Schicht.

## Datenquellen

- Sonnendach, Bundesamt für Energie, über `api3.geo.admin.ch`: Adresssuche
  (`SearchServer`) und Dachflächen (`MapServer/identify`, Ebene
  `ch.bfe.solarenergie-eignung-daecher`). Frei, ohne Schlüssel, erlaubt
  Abfragen aus dem Browser.
- Wetter: open-meteo, frei, ohne Schlüssel. Fällt die Abfrage aus, zeigt die
  Tafel nur den Sonnenstand.
