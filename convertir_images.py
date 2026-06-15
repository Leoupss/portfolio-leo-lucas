#!/usr/bin/env python3
"""Convertit toutes les photo.jpg/jpeg en photo.webp dans content/faune/ et content/flore/."""

from pathlib import Path
from PIL import Image

SCRIPT_DIR = Path(__file__).parent
SEARCH_DIRS = [SCRIPT_DIR / "content" / "faune", SCRIPT_DIR / "content" / "flore"]
TARGET_NAMES = {"photo.jpg", "photo.jpeg"}


def convert(src: Path) -> None:
    dest = src.with_suffix(".webp")
    with Image.open(src) as img:
        img.save(dest, "WEBP", quality=80)
    src.unlink()


def main():
    photos = [
        f
        for d in SEARCH_DIRS
        if d.exists()
        for f in d.rglob("*")
        if f.is_file() and f.name.lower() in TARGET_NAMES
    ]

    if not photos:
        print("Aucune image à convertir.")
        return

    errors = 0
    for i, photo in enumerate(photos, 1):
        try:
            convert(photo)
            print(f"[{i}/{len(photos)}] {photo.relative_to(SCRIPT_DIR)}")
        except Exception as e:
            print(f"[{i}/{len(photos)}] ERREUR {photo.relative_to(SCRIPT_DIR)} : {e}")
            errors += 1

    converted = len(photos) - errors
    print(f"\n{converted} image(s) convertie(s) en WebP.")


if __name__ == "__main__":
    main()
