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
- [ ] **VES-012** · 03.11.2026 · **Auftragsfotos von Adrian**: 98 Fotos vom
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
- [ ] **VES-020** · 03.11.2026 · **Adrians Fotos in den Slider**. Weiterhin
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
