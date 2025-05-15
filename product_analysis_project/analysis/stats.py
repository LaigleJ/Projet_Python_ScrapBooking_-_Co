import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans

def load_books(filepath: str) -> pd.DataFrame:
    # Charger le CSV
    df = pd.read_csv(filepath)

    # Nettoyer et convertir la colonne 'price'
    # Supprimer les symboles (€, virgules) si jamais présents, puis convertir proprement
    df['price'] = df['price'].replace('[^\d\.]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    return df

def describe_prices(df):
    print("📊 Statistiques sur les prix :")
    print("Moyenne :", df['price'].mean())
    print("Médiane :", df['price'].median())
    print("Écart-type :", df['price'].std())
    print("Minimum :", df['price'].min())
    print("Maximum :", df['price'].max())
    print("1er quartile (Q1) :", df['price'].quantile(0.25))
    print("3e quartile (Q3) :", df['price'].quantile(0.75))

def availability_counts(df):
    print("\n📦 Disponibilité des livres :")
    print(df['availability'].value_counts())

    print("\n📦 Disponibilité par niveau de rating :")
    grouped = df.groupby(['rating', 'availability']).size().unstack(fill_value=0)
    print(grouped)

def summary_by_rating(df):
    print("\n⭐ Prix moyen par rating :")
    mean_prices = df.groupby('rating')['price'].mean().sort_index()
    print(mean_prices)

def plot_price_histogram(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Histogramme des prix")
    plt.xlabel("Prix")
    plt.ylabel("Nombre de livres")
    plt.grid(True)
    os.makedirs("data", exist_ok=True)
    plt.savefig("data/histogram_price.png")
    plt.close()
    print("📈 Histogramme enregistré → data/histogram_price.png")

def plot_price_boxplot(df):
    plt.figure(figsize=(5, 6))
    plt.boxplot(df['price'], vert=True)
    plt.title("Boxplot des prix")
    plt.ylabel("Prix")
    os.makedirs("data", exist_ok=True)
    plt.savefig("data/boxplot_price.png")
    plt.close()
    print("📦 Boxplot enregistré → data/boxplot_price.png")

def plot_price_clusters(df):
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(df[['price']])

    plt.figure(figsize=(8, 5))
    plt.scatter(df.index, df['price'], c=df['cluster'], cmap='viridis', s=10)
    plt.title("Clustering des livres par prix")
    plt.xlabel("Index")
    plt.ylabel("Prix")
    os.makedirs("data", exist_ok=True)
    plt.savefig("data/clustering_price.png")
    plt.close()
    print("🎯 Clustering enregistré → data/clustering_price.png")

def plot_cluster_distribution(df):
    plt.figure(figsize=(8, 6))
    df.boxplot(column='price', by='cluster', grid=True)
    plt.title("Boxplot des prix par cluster")
    plt.suptitle("")
    plt.xlabel("Cluster")
    plt.ylabel("Prix")
    os.makedirs("data", exist_ok=True)
    plt.savefig("data/cluster_boxplot.png")
    plt.close()
    print("📦 Boxplot par cluster → data/cluster_boxplot.png")

def price_clustering(df):
    X = df[['price']]
    model = KMeans(n_clusters=3, random_state=42, n_init='auto')
    df['price_cluster'] = model.fit_predict(X)
    print("✅ Clustering des prix effectué.")
    return df

def summary_by_cluster(df):
    print("\n📊 Statistiques par gamme de prix (cluster) :")
    summary = df.groupby('price_cluster')['price'].describe()
    print(summary)
    return summary
