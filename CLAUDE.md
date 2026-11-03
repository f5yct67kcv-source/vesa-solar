# Arbeitsweise in diesem Repository

Kundenprojekt von formateins für die VeSa Solar GmbH. Die Regeln aus dem
formateins-Repository gelten sinngemäss, hier das Wichtigste.

## Logbuch

Jeder Entscheid und jede Aufgabe kommt in `LOGBUCH.md`, mit fortlaufender
Nummer **VES-…**, Datum, kurzem Satz und Beleg. `[x]` erledigt und belegt,
`[ ]` offen. Nummern nie neu vergeben, ein geänderter Entscheid bekommt eine
neue Nummer mit Verweis. Eintrag im selben Commit wie die Änderung, im Chat die
Nummer nennen. Vor der Arbeit `LOGBUCH.md` lesen. Vor einer neuen Nummer
`git fetch origin main` und die nächste freie nach der höchsten auf
`origin/main` nehmen.

## Entscheiden tut Adrian

Gestaltung erst vorführen, dann bauen: Entwürfe als Bild rendern (Playwright,
lokal über `python3 -m http.server`) und zur Wahl stellen. Steht nur ein Text
zur Wahl, kommen die Varianten als Text in den Chat. Technik (reines HTML
oder Astro) entscheidet Adrian vor dem ersten Bauschritt.

## Gestaltung

Farben nur aus dem Logo (Graustufen, siehe README). Keine Akzentfarbe
einführen, ohne zu fragen. Hell und dunkel immer beide prüfen.

## Schreibstil

Wie formateins (Entscheid vom 26.10.2026): Titel als Hook, der ein Ergebnis
verspricht. Kurze Sätze, ein Gedanke pro Satz. Schweizer Rechtschreibung ohne
ß, Beträge als CHF 2'400. Keine leeren Werbewörter. Anrede: in den Entwürfen
du, Entscheid mit VeSa offen (VES-005). Hier spricht VeSa in der Wir-Form,
nicht Adrian.

## Zahlen

Zahlen auf der Seite müssen von VeSa stammen. Geschätzte Zahlen in Entwürfen
sind als Schätzung markiert und gehen nie live.

## Push

Es gibt noch keinen Deploy. Sobald einer eingerichtet ist, heisst ein Push auf
`main` live, und es gilt dasselbe wie bei formateins: nur mit Adrians Wort.
