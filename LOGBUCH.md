# Logbuch vesa-solar.ch

Jeder Entscheid und jede Aufgabe bekommt eine Nummer **VES-…**, die nie
wiederverwendet wird. `[x]` heisst erledigt und belegt, `[ ]` heisst offen.
Die Vorgeschichte steht im formateins-Logbuch unter ENT-078 bis ENT-082.

## Einträge

- [x] **VES-001** · 02.11.2026 · Ideenfindung für das Redesign (Adrian:
  «komplettes redisgn … die seite soll sich von der konkurrenz abheben»).
  Heutige Seite und vier Schweizer Solar-Websites angeschaut. Befund: alle
  verkaufen Anlagen, niemand zeigt die Montage. Idee «Die Monteure», zehn
  Bausteine. Beleg: `IDEEN.md`, formateins ENT-078.
- [x] **VES-002** · 02.11.2026 · Drei grobe Richtungen A Baustelle, B Seetal,
  C Modulraster gerendert. Beleg: `entwuerfe/entwurf-a.html` bis `-c.html`,
  formateins ENT-079.
- [x] **VES-003** · 03.11.2026 · Adrian: «Zuerst halte dich an das Logo. Die
  Idee mit den Zahlen finde ich gut. Von de Farbe nicht.» Farben nur aus dem
  Logo, Graustufen, keine Akzentfarbe; Serife wie «VeSa» im Logo. Entwurf D
  hell und dunkel. Beleg: `entwuerfe/entwurf-d-*.html`, formateins ENT-080.
- [x] **VES-004** · 03.11.2026 · Adrian: «D mit switch hell/dunkel … mir
  fehlt allerdings das gewisse extra … die seite darf auch technisch mehr
  zeigen». Entwurf E: Schalter, Dach-Abfrage beim Bund (Sonnendach), Live-Tafel
  mit Sonnenstand und Wetter, Montagesystem im Schnitt mit Schieber. Beleg:
  `entwuerfe/entwurf-e.html`, formateins ENT-081.
- [ ] **VES-005** · 03.11.2026 · Offene Entscheide vor dem Bau: du oder Sie
  (Entwürfe duzen), Hochdeutsch oder Mundart im Titel, Technik reines HTML oder
  Astro (Empfehlung Astro wegen wachsender Referenzen und wiederkehrender
  Bausteine), wer die Referenzen pflegt.
- [ ] **VES-006** · 03.11.2026 · Von VeSa zu beschaffen: Liste aller Anlagen
  (Ort, Module, kWp, Dachart, Neigung, Ausrichtung, Montagetage, Jahr), Logo
  als Vektor (SVG oder PDF), Fotos in Originalgrösse, Zustimmung der
  Mitarbeitenden für Fotos auf der Seite. Bis dahin sind alle Zahlen ausser
  Muri 292 und Luzern 189 Module geschätzt.
- [x] **VES-007** · 03.11.2026 · Eigenes Repository angelegt (Adrian: «repo
  ist angelegt»), Stand der Entwürfe aus formateins übernommen, erster Commit
  auf `main`. Kein Deploy. Offen: Vorschau. Vorschlag GitHub Pages auf `main`
  einschalten (Settings → Pages), dann ist Entwurf E mit funktionierender
  Dach-Abfrage als Link zu öffnen; das Repository ist öffentlich, die Fotos
  stammen von der heutigen öffentlichen Seite. Entscheid Adrian. Erledigt:
  Adrian hat Pages auf `main` eingeschaltet, Vorschau unter
  `https://f5yct67kcv-source.github.io/vesa-solar/entwuerfe/` (Antwort 200).
- [ ] **VES-008** · 03.11.2026 · Ideen für weitere technische Teile, noch
  nicht gebaut: Schweizer Karte mit allen Dächern, Baustellen-Ticker aus
  Instagram, Schnittzeichnung auch für Indach und Flachdach, «kW jetzt» in der
  Nacht durch den Tageshöchstwert ersetzen.
- [x] **VES-009** · 03.11.2026 · **Logo als Vektor selbst erzeugt** (Adrian:
  «VeSa Vektor selbst erzeugen»). Dreieck exakt als Geometrie nachgebaut:
  gleichseitig, neun Dreiecke in drei Reihen, Farben gemessen und als
  Prozent Schwarz bestätigt (K20 `#cccccc`, K30 `#b3b3b3`, K40 `#999999`,
  K50 `#808080`, K70 `#4d4d4d`, K90 `#1a1a1a`). Schrift «VeSa» und «Solar
  GmbH» aus dem PNG in sechsfacher Auflösung nachgezeichnet (potrace).
  Abweichung zum Original: 0,14 % der Pixel, nur an Kanten. Dateien in
  `marke/`: `vesa-logo.svg`, `vesa-logo-negativ.svg` (Grautöne gespiegelt wie
  in Entwurf D dunkel), `vesa-bildmarke.svg`, `favicon.svg`, dazu PNG mit
  2000 px. Entwürfe D und E nutzen jetzt das SVG und die exakten Grautöne,
  E hat das Favicon. Beleg `28c0504`. Offen: Ob das Negativ so bleiben soll
  oder das Dreieck im Original-Grau auf dunklem Grund steht, ist eine Frage
  an VeSa.
- [x] **VES-010** · 03.11.2026 · Adrian: «freigabe bestätigt». Verstanden als
  Einverständnis für Fotos des Teams auf der Seite (Teil von VES-006). Offen
  aus VES-006 bleiben die Anlagenliste und die Fotos in Originalgrösse.
- [x] **VES-011** · 03.11.2026 · **Fehler in der Live-Tafel** behoben: Die
  Formel für das Julianische Datum lag einen halben Tag daneben, darum stand
  die Sonne um 10 Uhr bei −50° und Auf- und Untergang waren vertauscht.
  Geprüft gegen bekannte Werte: 21. Juni 13:30 Höhe 66,1°, 21. Dezember 12:20
  Höhe 19,2°, 3. November Aufgang 07:14, Untergang 17:08. Tagesbogen rechnet
  in Zürcher Zeit, auch für Besucher in anderen Zeitzonen. Nachts zeigt die
  Zählerleiste den Wert von heute Mittag statt 0 kW (aus VES-008). Beleg
  `28c0504`.
- [x] **VES-012** · 03.11.2026 · **Auftragsfotos von Adrian**: 98 Fotos vom
  18.06.2026 im Google-Drive-Ordner «VESA Solar» (A7408035 bis A7408132,
  je 6 bis 23 MB). Der Drive-Zugang dieser Sitzung bricht bei Dateien dieser
  Grösse ab, und ohne Freigabe leitet Google auf die Anmeldung um. Offen:
  Adrian gibt den Ordner per Link frei («Jeder mit dem Link, Betrachter») oder
  legt verkleinerte Kopien (etwa 2500 px) ab. Dann Auswahl und Einbau.
- [ ] **VES-013** · 03.11.2026 · **Gruppenfoto des Teams fehlt** (Adrian:
  «Gruppe, Team fehlt noch»). Für die Startseite (Team-Block) und «Über uns».
  Offen: Termin mit VeSa, Bildliste vorher abstimmen.
- [ ] **VES-014** · 03.11.2026 · Adrian fragt nach dem Grund für Astro.
  Begründung im Chat: Datenblatt pro Dach aus einer Vorlage, Bilder
  automatisch verkleinert, Bausteine einmal gebaut, Zähler aus der Liste.
  Entscheidende Frage: Bekommt jedes Dach eine eigene Seite? Entscheid HTML
  oder Astro weiter offen (VES-005).
- [x] **VES-015** · 03.11.2026 · **Kopf auf dem Handy** nach Adrians
  Bildschirmfoto: «Das Logo präsenter, grösser. Trennstrich weg. Hamburger
  Menu mit Dropdown, dort auch hell/dunkel. Tel. Nr. in Kontakt». Entwurf E,
  nur unter 900 px Breite: Logo 88 px statt 58 px hoch, Kopf ohne Linie,
  Telefonknopf raus. Neu ein Hamburger rechts, der sich zum Kreuz dreht, und
  ein Dropdown mit den vier Menüpunkten, einem Block «Kontakt» (Telefon gross
  und anwählbar, E-Mail, Adresse) und dem Schalter «Darstellung Hell /
  Dunkel». Ein Menüpunkt «Kontakt» war zuerst auch drin, ist wieder raus,
  weil er den Kontaktblock doppelte. Menü schliesst beim Antippen eines
  Punkts und mit Escape. Desktop unverändert, dort ist die Nummer jetzt
  ebenfalls anwählbar. Geprüft mit Playwright auf 390 px, hell und dunkel,
  offen und zu, ohne Skriptfehler. Renderings in `entwuerfe/bilder/`. Beleg `9dbc19c`.
- [ ] **VES-016** · 03.11.2026 · **Logofarben als Verlauf über die ganze
  Seite**, Beispiele zur Wahl (Adrian: «Ich möchte die Farben des Logos auch
  im Verlauf des Hintergrund, verteilt auf die ganze Seite … Zeig mir mal
  Beispiele»). Eigene Datei `entwuerfe/entwurf-e-verlauf.html`, Entwurf E
  bleibt unverändert. Idee: Die Seite steigt das Dreieck hinab, oben hell wie
  die Spitze, unten dunkel wie die Basis. Hell: Weiss, Weiss, K20, K30, K40,
  K50, K70, K90, K100 auf die neun Abschnitte. Dunkel: K90 und K70 im
  Wechsel, unten K100. Schrift wechselt ab K70 auf Weiss, bis K50 bleibt sie
  schwarz. Drei Varianten über `?bg=`: **1 Fliessend** (weicher Verlauf,
  jede Farbe in der Mitte ihres Abschnitts), **2 Stufen** (jeder Abschnitt
  eine Fläche), **3 Facetten** (Dreiecksraster wie im Logo, Grauton nach
  Höhe, je eine Stufe heller oder dunkler, halb deckend über dem Verlauf).
  Karten werden durchscheinend, der Kopf nimmt die Farbe oben an und ist
  leicht unscharf hinterlegt. Fehler beim ersten Rendern behoben: Der
  Kontaktblock bekam die falsche Schriftfarbe, weil `.cta` zuerst den
  Telefonknopf traf. Geprüft hell und dunkel, Desktop und Handy, ohne
  Skriptfehler. Renderings `entwuerfe/bilder/verlauf-*.jpg`. Offen: Adrian
  wählt eine Variante oder verwirft die Idee.
- [x] **VES-017** · 03.11.2026 · **Verlauf vorerst verworfen** (Adrian:
  «Vorerst verwerfen, passt nicht»). Löst VES-016 ab. Die Datei
  `entwuerfe/entwurf-e-verlauf.html` bleibt als Beleg liegen, in der
  Übersicht als verworfen markiert.
- [ ] **VES-018** · 03.11.2026 · **Foto im Kopf, als Einzelbild oder
  Slider** (Adrian, mit Bildschirmfoto des Vorschlags für Ammann
  Raumgestalter: «Ich möchte bereits im Hero-Bereich ein Foto verwenden oder
  sogar Slider-Foto»). Eigene Datei `entwuerfe/entwurf-e-hero.html`, Entwurf
  E bleibt unverändert. `?hero=1` ein Foto, `?hero=2` Slider mit vier
  Dächern (Luzern Steildach, Muri Flachdach, Spreitenbach Industrie, Zürich
  Indach), Wechsel alle 6 s mit leichtem Heranzoomen, Balken mit
  Fortschritt zum Antippen, Wischen auf dem Handy, Pause bei verstecktem
  Tab, kein automatischer Wechsel bei «Bewegung reduzieren». Karte oben
  rechts mit Ort, Dachart, Modulzahl und Link zu allen Dächern. Der Kopf ist
  in hell und dunkel dunkel hinterlegt, weil das Foto in Dunkel ausläuft.
  Handy: Foto zuoberst, Titel im Übergang, breiter runder Knopf «Dein Dach
  prüfen», darunter «15 Jahre auf dem Dach», «Mitglied Swissolar», ein
  kurzer Live-Hinweis zur Sonne und die Balken, alles im ersten Bildschirm
  (Balken enden bei 787 von 844 px). Desktop: Foto über die ganze Breite,
  Text links auf Abdunklung, Live-Tafel rechts unten. Modulzahlen ausser
  Muri und Luzern geschätzt. Geprüft hell und dunkel, Handy und Desktop,
  ohne Skriptfehler, Taktung gemessen (Wechsel nach 6 s, Antippen springt
  sofort). Renderings `entwuerfe/bilder/kopf-*.jpg`. Offen: Adrian wählt
  Foto oder Slider, dann kommt es in Entwurf E. Später mit den eigenen
  Auftragsfotos (VES-012).
- [x] **VES-019** · 03.11.2026 · **Slider gewählt** (Adrian: «Slider mit
  meinen Fotos»), schliesst die Wahl aus VES-018. Der Slider steckt jetzt in
  `entwuerfe/entwurf-e.html`, vorerst mit den vier Fotos von der heutigen
  VeSa-Seite. `entwurf-e-hero.html` bleibt als Beleg. Neues Skript
  `werkzeuge/fotos-aufbereiten.py`: dreht Originale nach EXIF, entfernt die
  Metadaten (GPS, Kamera), schreibt WebP in 2400, 1600 und 900 px für
  `srcset` und einen Kontaktbogen zur Auswahl. An zwei Fotos geprüft.
  Renderings von E neu, hell und dunkel, ohne Skriptfehler.
- [x] **VES-020** · 03.11.2026 · **Adrians Fotos in den Slider**. Weiterhin
  blockiert wie in VES-012: Der Drive-Ordner «VESA Solar» ist privat (Google
  leitet auf die Anmeldung um, um 12:20 erneut geprüft), und der
  Drive-Zugang dieser Sitzung bricht bei Dateien ab etwa 6 MB ab.
  Empfohlener Weg: Ordner vorübergehend per Link freigeben («Jeder mit dem
  Link», Betrachter), herunterladen, Freigabe zurücknehmen. Originale
  **nicht** ins Repository hochladen: Es ist öffentlich, die Git-Geschichte
  behält sie auch nach dem Löschen, und die Kamera-Metadaten können den
  Standort des Kundenhauses enthalten. Ins Repository kommen nur die vom
  Skript aufbereiteten WebP ohne Metadaten. Danach Kontaktbogen zeigen,
  Adrian wählt die vier bis sechs Slider-Bilder und je Bild Ort, Dachart
  und Modulzahl.
- [x] **VES-021** · 03.11.2026 · **Slider mit Adrians Fotos**, erledigt
  damit VES-012 und VES-020. Adrian hat den Drive-Ordner per Link
  freigegeben («Link geändert»). Alle 98 Fotos geladen (1,6 GB, alle gültig,
  Sony ILCE-7M4, 18.06.2026, 07:29 bis 12:58). Sie zeigen einen Montagetag:
  Unterbau am Morgen, Transportdrohne auf der Wiese, Pilot auf dem Kamin,
  Module hängen an der Drohne, das Team nimmt sie auf dem Gerüst an. Fünf
  Bilder für den Slider gewählt, das stärkste zuerst: A7408094 «Module
  kommen per Drohne aufs Dach» (09:52), A7408110 «Oben nimmt das Team sie
  an» (10:10), A7408084 «Der Pilot fliegt vom Kamin aus» (09:44), A7408043
  «Unterbau ab halb acht» (07:33), A7408062 «Drohne startklar» (09:06).
  Balken: Drohne, Team, Pilot, Unterbau, Start. Aufbereitet mit
  `werkzeuge/fotos-aufbereiten.py` nach `fotos/auftrag/`, je 900, 1600 und
  2400 px, ohne Metadaten, zusammen 1,8 MB; im Slider mit `srcset`, das
  Handy lädt 900 px. Bildausschnitt je Foto getrennt für Handy und Desktop.
  Auf dem Handy zeigt die Karte nur Titel und Uhrzeit. Kontaktbögen aller 98
  Fotos in `fotos/auftrag/uebersicht/`, Originale nur in der Sitzung, nicht
  im Repository. Geprüft: alle fünf Bilder hell und dunkel, Handy und
  Desktop, keine fehlenden Dateien, keine Skriptfehler. Offen: Ort der
  Baustelle für die Karte (heute nur Datum und Uhrzeit), ob die Drohne
  VeSa gehört oder einem Partner (Text «per Drohne» bewusst neutral), und
  Adrian nimmt die Drive-Freigabe zurück. Desktop: Beim Unterbau-Bild liegt
  der Monteur unter dem Text, weil das Foto keinen Spielraum nach rechts
  hat.
- [ ] **VES-022** · 03.11.2026 · **Balken weg, Karte dünn oder ohne**
  (Adrian, Bildschirmfoto vom Handy mit eingekreister Karte: «Balken
  entfernen. Auch der obere Balken ist dick. Zeig mir den Balken dünner und
  einmal ganz ohne nur als Bild»). Die Balken unter dem Kopf (Drohne, Team,
  Pilot, Unterbau, Start) sind entfernt, Markup und Stil. Der Slider wechselt
  weiter alle 6 s und lässt sich wischen. Die Karte oben rechts ist jetzt
  eine dünne Zeile: Uhrzeit in Mono, Titel, Pfeil, halb durchsichtig
  hinterlegt, 29 px hoch statt rund 90 px; zu lange Titel werden mit «…»
  gekürzt statt abgeschnitten (Adrians Bildschirmfoto zeigte den Titel
  rechts abgeschnitten). Die Karte zeigt nur noch die Uhrzeit, ohne Datum
  und Zusatz. Variante ohne Karte über `?cap=ohne`. Geprüft auf 375 und 390
  px, hell und dunkel, Desktop, ohne Skriptfehler. Renderings
  `entwuerfe/bilder/karte-duenn-ohne-*.jpg`. Offen: Adrian wählt dünn oder
  ohne; heute steht dünn als Vorgabe in Entwurf E.
- [ ] **VES-023** · 03.11.2026 · **Zweiter Fotosatz aus Dropbox** (Adrian:
  Link auf den Ordner «Baustelle Sändu 2», «Kannst du hier draufgreifen?»).
  Erreichbar, als ZIP 2,1 GB, 109 JPG, Sony ILCE-7M4, 04.09.2025, 09:30 bis
  13:30. Inhalt: fertige Anlage auf den Dächern eines
  Landwirtschaftsbetriebs. Hallen mit grossen Modulflächen in der
  Landschaft, ein Feldweg zum Hof, der Hofhund, zwei Monteure im
  VeSa-Shirt auf dem Hofplatz und ab 13:27 auf dem Dach zwischen
  Modulreihen und Lüftungshauben. Keine Montageaufnahmen. Sicher entpackt,
  Kontaktbögen erstellt, ZIP gelöscht. Nichts davon im öffentlichen
  Repository, weil die Bilder den Hof erkennbar zeigen (Hofschild).
  Vorschlag: Referenz mit Datenblatt und zwei Slider-Bilder (A7407673
  Monteur am Dachfirst zwischen den Modulen, A7407664 Modulfeld mit Wald).
  Offen: Adrian sagt, wofür; Ort, Module, kWp und das Einverständnis des
  Hofs.
- [x] **VES-024** · 03.11.2026 · **Erstes Slider-Bild getauscht** (Adrian
  schickt ein Bild: «verwende dieses, das andere ist unscharf. etwas
  hineinzoomen wegen des Kamins»). Das Bild ist A7408112 (10:10, per
  Bildvergleich gefunden, Übereinstimmung 0,98), es ersetzt A7408094 als
  erstes Bild «Module kommen per Drohne aufs Dach», gleicher Moment, das
  Modul schwebt über dem Team. Aus dem Original zugeschnitten: 80 % der
  Fläche, links 20 % weg, damit der Kamin nur noch am Rand steht, oben
  bündig, damit das Modul ganz bleibt. Aufbereitet als
  `fotos/auftrag/modul-annahme-*.webp`, die alten Dateien
  `drohne-anflug-*.webp` entfernt, Kontaktbogen neu. Uhrzeit in der Karte
  jetzt 10:10. Geprüft auf 375 und 390 px und Desktop, hell und dunkel,
  keine fehlenden Dateien, keine Skriptfehler. Annahme: «das andere» meint
  das erste Bild mit demselben Motiv; falls das Team-Bild gemeint war, ist
  der Tausch ein Schritt.
- [x] **VES-025** · 03.11.2026 · **Slider-Fotos waren auf dem Handy
  unscharf** (Adrian: «Warum ist deine Foto unscharf?!»). Ursache gemessen,
  nicht das Foto, sondern die Seite: (1) `sizes="100vw"` war falsch, weil
  das Bild den Kopf mit `object-fit: cover` füllt und auf dem Handy rund
  634 statt 390 CSS-Pixel breit angezeigt wird. Ein Handy mit 2-facher
  Auflösung lud darum 900 px für nötige 1266 px (1,4-fach hochgerechnet),
  ein iPhone 1600 px für 1899 px (1,2-fach). (2) Die grösste Fassung mit
  2400 px reichte für Retina-Desktops nicht (nötig 2880 px). (3) Das
  langsame Heranzoomen lief die ganzen 6 s, Safari zeigt Bilder während
  einer solchen Bewegung weicher. Behoben: `sizes="(max-width: 900px)
  760px, 100vw"`, zusätzliche Fassung 3200 px, WebP-Qualität 82 statt 78
  (`werkzeuge/fotos-aufbereiten.py`), Zoom entfernt, Überblenden bleibt.
  Jetzt lädt das iPhone 2400 px für 1902 px, das Handy 2x 1600 px für
  1268 px, der Retina-Desktop 3200 px für 2880 px, nirgends wird
  hochgerechnet. Vergleich am selben Ausschnitt: Kantenschärfe +44 %
  (`entwuerfe/bilder/schaerfe-vergleich.jpg`). Fünf Slider-Bilder neu
  aufbereitet, zusammen 4,4 MB in vier Grössen; ein Handy lädt pro Bild
  etwa 100 bis 330 KB.
- [ ] **VES-026** · 03.11.2026 · **Webseite immer noch unscharf** (Adrian,
  Screenshot vom Mac neben seiner Vorlage: «vergleiche mal die Bilder!!
  Webseite ist doch nicht scharf?»). Gemessen statt behauptet: Sein Fenster
  ist rund 1920 CSS-Pixel breit mit Retina, das Bild füllt den Kopf über die
  ganze Breite und wird darum fast in Originalgrösse gezeigt; seine Vorlage
  zeigt das ganze Foto nur 1536 px breit. Die Datei auf der Seite ist so
  scharf wie das Original (Gesichtsvergleich
  `entwuerfe/bilder/gesicht-original-datei-screenshot.jpg`), aber das
  Original A7408112 ist bei 100 % selbst weich: Arme in Bewegung, Gesicht
  leicht unscharf. Gross gezeigt wird das sichtbar. Massnahmen:
  `werkzeuge/fotos-aufbereiten.py` schärft nach dem Verkleinern leicht nach
  (Unscharf maskieren, Radius 1, 70 %), grösste Fassung 3840 statt 3200 px
  für 1920er Retina-Bildschirme, alle Slider-Bilder neu. Schärfe aller
  Aufnahmen der Serie gemessen: A7408113 und A7408114 (eine Sekunde später)
  sind etwa doppelt so scharf wie 112. A7408113 links ohne Kamin
  zugeschnitten als `modul-griff`, in der Vorschau anwählbar mit
  `?erstes=113`. Vergleich `entwuerfe/bilder/vergleich-112-113-*.jpg`.
  Offen: Adrian wählt 112 (nachgeschärft) oder 113.
- [x] **VES-027** · 03.11.2026 · **Team-Bild aus dem Slider entfernt**
  (Adrian, Screenshot des Bilds «Oben nimmt das Team sie an», A7408110:
  «dieses foto entfernen!»). Aus `entwuerfe/entwurf-e.html` genommen, die
  Dateien `fotos/auftrag/team-geruest-*.webp` gelöscht, Kontaktbogen neu.
  Der Slider zeigt jetzt vier Bilder: Module per Drohne, Pilot auf dem
  Kamin, Unterbau, Drohne startklar. Wechsel im Browser geprüft, keine
  Skriptfehler, keine fehlenden Dateien. Die Wahl 112 oder 113 für das
  erste Bild bleibt offen (VES-026).
- [x] **VES-028** · 03.11.2026 · **Vergleich «dünn / ohne» mit dem aktuellen
  Bild** (Adrian, Bildschirmfoto von `karte-duenn-ohne-desktop.jpg`: «dieses
  Bild mit dem aktuell ersetzen»). Die Renderings aus VES-022 zeigten noch
  das alte erste Bild und das Team-Foto. Neu gerendert mit dem heutigen
  Slider (erstes Bild 112, vier Bilder nach VES-027): Desktop 1440 px und
  Handy 375/390 px, hell und dunkel, ohne Skriptfehler. Die Wahl dünn oder
  ohne bleibt offen (VES-022).
- [x] **VES-029** · 03.11.2026 · **Erstes Bild wieder A7408094** (Adrian,
  zum Vergleich aus VES-028: «nein das bild nehmen wo ich geschickt habe im
  beispiel!»). Gemeint ist das Bild aus dem alten Vergleich: A7408094
  «Module kommen per Drohne aufs Dach», 09:52, drei Monteure auf dem Gerüst,
  das Modul hängt schräg an der Drohne. Die Annahme aus VES-024 war falsch:
  A7408112 sollte nicht A7408094 ersetzen. A7408094 ist neu aufbereitet,
  ganzes Bild, nachgeschärft, 900 bis 3840 px
  (`fotos/auftrag/drohne-anflug-*.webp`). Entfernt: A7408112
  (`modul-annahme-*`) und A7408113 (`modul-griff-*`, `?erstes=113`). Damit
  ist die Wahl aus VES-026 hinfällig. Beide lassen sich aus dem Verlauf
  zurückholen. Kontaktbogen und Vergleich `karte-duenn-ohne-*.jpg` sind neu.
  Geprüft auf 390 px (lädt 2400 px) und 1920 px Retina (lädt 3840 px),
  ohne fehlende Dateien und ohne Skriptfehler.
- [ ] **VES-030** · 03.11.2026 · **Variante: Bildfläche fest 2:1 auf dem
  Desktop** (Adrian: «zeig mir die Bildfläche fest auf 2:1»; vorher die
  Frage, welches Seitenverhältnis die Bilder brauchen, damit nichts
  zugeschnitten wird). Heute ist die Fläche so breit wie das Fenster und
  höchstens 820 px hoch, darum 1,8:1 bis 3,1:1 je nach Bildschirm. Die
  Variante `?flaeche=2zu1` stellt sie ab 901 px Breite fest auf 2:1, das
  Handy bleibt gleich. Gemessen: 1280×720 Fläche 1280×640, 1440×900
  1440×720, 1920×1080 1920×960, 2560×1440 2560×1280. Bilder im Format 2:1
  werden damit auf keinem Desktop beschnitten. Dafür wird der Kopf auf
  breiten Bildschirmen hoch, und die Zahlenleiste rutscht unter den
  Fensterrand. Vergleich `entwuerfe/bilder/flaeche-2zu1-*.jpg`, ohne
  Skriptfehler. Offen: Adrian wählt heute oder 2:1.
