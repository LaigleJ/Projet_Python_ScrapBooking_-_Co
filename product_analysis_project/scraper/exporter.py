# Ce fichier contient le code pour le scraper de livres.

import csv
from .book import Book
import os  # Si tu veux créer automatiquement les dossiers

def export_books_to_csv(books: list[Book], filename: str = "data/books.csv"):
    if not books:
        print("⚠️ Aucun livre à exporter.")
        return

    # Crée le dossier si nécessaire
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "availability", "rating"])
        writer.writeheader()

        for book in books:
            writer.writerow(book.to_dict())

    print(f"✅ Export terminé : {filename}")
