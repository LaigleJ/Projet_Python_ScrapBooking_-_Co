from scraper.scraper_books import BookScraper
from scraper.exporter import export_books_to_csv

def main():
    # Lancer le scraper pour collecter les livres
    scraper = BookScraper()
    
    # Scraper les 50 pages (ou un autre nombre de pages si tu veux moins de livres)
    books = scraper.scrape_all(pages=50)
    
    # Afficher le nombre total de livres récupérés
    print(f"Nombre total de livres récupérés : {len(books)}")
    
    # Exporter les livres dans le fichier CSV
    export_books_to_csv(books)

if __name__ == "__main__":
    main()