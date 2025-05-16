from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scraper.game import Game
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service


class GameScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")  # pas d'interface graphique
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)


    def scrape_page(self, url):
        self.driver.get(url)
        time.sleep(3)  # attendre le chargement complet
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        games = []
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for result in results:
            try:
                title = result.h2.text.strip()
                price_whole = result.find('span', class_='a-price-whole')
                price_frac = result.find('span', class_='a-price-fraction')
                if price_whole and price_frac:
                    price = float(price_whole.text.replace(',', '').replace('.', '') + "." + price_frac.text)
                else:
                    continue
                availability = "Amazon"  # Info non disponible directement
                rating_elem = result.find('span', class_='a-icon-alt')
                rating = rating_elem.text if rating_elem else "No rating"
                games.append(Game(title, price, availability, rating))
            except Exception as e:
                print(f"Erreur : {e}")

        return games

    def close(self):
        self.driver.quit()

    def scrape_all(self, pages=1):
        base_url = "https://www.amazon.fr/s?k=jeux+de+société+2+joueurs&page="
        all_games = []
        for i in range(1, pages + 1):
            url = base_url + str(i)
            print(f"Scraping page {i}...")
            games = self.scrape_page(url)
            all_games.extend(games)
        self.close()
        return all_games
