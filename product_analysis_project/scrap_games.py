from scraper.scraper_games import GameScraper
from scraper.exporter import export_games_to_csv
from analysis.stats_games import load_games, describe_prices, availability_counts, summary_by_rating, plot_price_histogram, plot_price_boxplot, price_clustering, plot_price_clusters, summary_by_cluster

scraper = GameScraper()
games = scraper.scrape_all(pages=2)
export_games_to_csv(games, "data/games.csv")

# Chargement des données
df = load_games("data/games.csv")

# Affichage des statistiques univariées
print(describe_prices(df))
print(availability_counts(df))
print(summary_by_rating(df))

# Visualisations
plot_price_histogram(df)
plot_price_boxplot(df)

# Clustering des prix
df = price_clustering(df)
plot_price_clusters(df)
print(summary_by_cluster(df))
