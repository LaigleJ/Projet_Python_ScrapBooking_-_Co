# Ce fichier contient le code pour le scraper de livres.
from analysis.stats import (
    load_books,
    describe_prices,
    availability_counts,
    summary_by_rating,
    price_clustering,
    summary_by_cluster,
    plot_price_histogram,
    plot_price_boxplot,
    plot_price_clusters,
    plot_cluster_distribution
)

def main():
    # Charger les livres depuis le fichier CSV
    df = load_books('data/books.csv')

    # Afficher les premières lignes pour vérifier le nettoyage
    print(df.head())

    describe_prices(df)
    availability_counts(df)
    summary_by_rating(df)

    # Clustering
    df = price_clustering(df)
    summary_by_cluster(df)

     # Visualisations
    plot_price_histogram(df)
    plot_price_boxplot(df)
    plot_price_clusters(df)
    plot_cluster_distribution(df)
    
if __name__ == "__main__":
    main()
