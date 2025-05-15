# 📚 ScrapBooking & Co.

Un projet Python complet de **web scraping**, **analyse de données** et **visualisation** autour du site [Books to Scrape](https://books.toscrape.com).

## 🎯 Objectifs

- Scraper l’ensemble des livres du site Books to Scrape
- Stocker les données dans un fichier CSV
- Analyser les données avec pandas
- Visualiser les résultats avec matplotlib
- Segmenter les livres par gamme de prix grâce à l’algorithme K-Means

---

## 📁 Structure du projet

product_analysis_project/
├── scraper/
│ ├── init.py
│ ├── book.py # Classe Book
│ ├── scraper_books.py # Scraping du site books.toscrape.com
│ ├── scraper_custom.py # (à venir) Scraping d’un site e-commerce réel
│ └── exporter.py # Export CSV
├── analysis/
│ ├── init.py
│ └── stats.py # Analyses statistiques + visualisations
├── data/
│ ├── books.csv
│ ├── histogram_price.png
│ ├── boxplot_price.png
│ ├── clustering_price.png
│ └── cluster_boxplot.png
├── main.py # Script principal d'analyse
├── scrape_books.py # Script de scraping
└── README.md


## ⚙️ Installation

> 📌 Nécessite Python 3.8+  
> Installe les dépendances requises avec :

```bash
pip install pandas matplotlib scikit-learn requests beautifulsoup4 --user
🚀 Utilisation
1. Scraping des livres
Lance une seule fois pour récupérer tous les livres :

```bash
python scrape_books.py
Cela crée data/books.csv.

2. Analyse des données
```bash
python main.py
Ce script :

Charge les données

Affiche des statistiques descriptives

Fait un clustering des prix en 3 segments

Génère 4 fichiers de visualisation :

📊 data/histogram_price.png
📦 data/boxplot_price.png
🎯 data/clustering_price.png
📦 data/cluster_boxplot.png
📈 Fonctions disponibles (stats.py)

load_books() : charge et nettoie les données

describe_prices() : stats de base (moyenne, médiane…)

availability_counts() : disponibilité et rating

summary_by_rating() : prix moyen par rating

price_clustering() : ajoute la colonne price_cluster

summary_by_cluster() : stats par cluster

plot_price_histogram() : histogramme des prix

plot_price_boxplot() : boxplot simple

plot_price_clusters() : clustering avec K-Means

plot_cluster_distribution() : boxplot des prix par cluster