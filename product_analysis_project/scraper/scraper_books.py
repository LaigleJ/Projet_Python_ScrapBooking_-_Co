import requests
from bs4 import BeautifulSoup
from .book import Book
import time
import random

class BookScraper:
    BASE_URL = "https://books.toscrape.com/catalogue/"
    START_URL = "https://books.toscrape.com/index.html"

    def __init__(self):
        self.books = []

        # Simule un vrai navigateur
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            )
        }

    def scrape_page(self, url: str):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                print(f"⛔ Erreur {response.status_code} pour {url}")
                return []

            soup = BeautifulSoup(response.text, 'html.parser')
            book_elements = soup.select('article.product_pod')
            books = []

            for element in book_elements:
                title = element.h3.a['title']
                price = float(element.select_one('p.price_color').text[2:])  # Enlève le £
                availability = element.select_one('p.instock.availability').text.strip()
                rating = element.select_one('p.star-rating')['class'][1]

                book = Book(title, price, availability, rating)
                books.append(book)

            return books

        except requests.RequestException as e:
            print(f"⚠️ Exception lors de la requête : {e}")
            return []

    def scrape_all(self, pages=50):
        all_books = []

        # Scrape page 1 (index.html)
        print("📘 Scraping: index.html")
        all_books.extend(self.scrape_page(self.START_URL))
        time.sleep(random.uniform(1.0, 3.0))

        # Scrape pages suivantes
        for page in range(2, pages + 1):
            url = f"{self.BASE_URL}page-{page}.html"
            print(f"📘 Scraping: page-{page}.html")

            books = self.scrape_page(url)
            if not books:
                print(f"✅ Fin du scraping à la page {page} (aucune donnée trouvée).")
                break

            all_books.extend(books)
            time.sleep(random.uniform(1.0, 3.0))  # Pause aléatoire pour éviter les blocages

        self.books = all_books
        return all_books
