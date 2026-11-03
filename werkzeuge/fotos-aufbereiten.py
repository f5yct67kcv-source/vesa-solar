#!/usr/bin/env python3
"""Fotos für die Seite aufbereiten.

Nimmt Originale (JPG, auch 20 MB aus der Kamera), dreht sie nach EXIF richtig,
entfernt die Metadaten (GPS, Kamera) und schreibt WebP in drei Breiten für
srcset: 3200, 2400, 1600 und 900 px. Dazu ein Kontaktbogen zur Auswahl.

    python3 werkzeuge/fotos-aufbereiten.py ORDNER_MIT_ORIGINALEN fotos/auftrag

Ergebnis: fotos/auftrag/NAME-3200.webp, -2400.webp, -1600.webp, -900.webp und
fotos/auftrag/kontaktbogen.jpg. Die Originale bleiben, wo sie sind, und
kommen nicht ins Repository.
"""
import sys, pathlib
from PIL import Image, ImageOps, ImageDraw

BREITEN = (3200, 2400, 1600, 900)
QUALITAET = 82

def aufbereiten(quelle: pathlib.Path, ziel: pathlib.Path):
    ziel.mkdir(parents=True, exist_ok=True)
    dateien = sorted(p for p in quelle.iterdir() if p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.tif', '.tiff'))
    if not dateien:
        sys.exit(f'Keine Bilder in {quelle}')
    bogen = []
    for p in dateien:
        im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
        name = p.stem.lower().replace(' ', '-')
        for b in BREITEN:
            k = im.copy()
            if k.width > b:
                k = k.resize((b, round(k.height * b / k.width)), Image.LANCZOS)
            k.save(ziel / f'{name}-{b}.webp', 'WEBP', quality=QUALITAET, method=6)
        groesse = sum((ziel / f'{name}-{b}.webp').stat().st_size for b in BREITEN) // 1024
        print(f'{p.name}: {im.width}x{im.height} -> {name}-*.webp ({groesse} KB zusammen)')
        t = im.copy(); t.thumbnail((360, 240)); bogen.append((name, t))
    spalten = 5; zeilen = (len(bogen) + spalten - 1) // spalten
    k = Image.new('RGB', (spalten * 370, zeilen * 270), 'white'); d = ImageDraw.Draw(k)
    for i, (name, t) in enumerate(bogen):
        x, y = (i % spalten) * 370 + 5, (i // spalten) * 270 + 5
        k.paste(t, (x, y)); d.text((x, y + 244), name, fill='black')
    k.save(ziel / 'kontaktbogen.jpg', quality=82)
    print(f'{len(bogen)} Fotos, Kontaktbogen: {ziel / "kontaktbogen.jpg"}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    aufbereiten(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
