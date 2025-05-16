import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def load_games(filepath):
    df = pd.read_csv(filepath)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.dropna(subset=['price'], inplace=True)
    return df

def describe_prices(df):
    return df['price'].describe()

def availability_counts(df):
    return df.groupby(['availability', 'rating']).size()

def summary_by_rating(df):
    return df.groupby('rating')['price'].mean()

def plot_price_histogram(df):
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Répartition des prix des jeux")
    plt.xlabel("Prix (€)")
    plt.ylabel("Nombre de jeux")
    plt.savefig("data/histogram_games.png")
    plt.close()

def plot_price_boxplot(df):
    plt.boxplot(df['price'])
    plt.title("Boxplot des prix des jeux")
    plt.ylabel("Prix (€)")
    plt.savefig("data/boxplot_games.png")
    plt.close()

def price_clustering(df):
    X = df[['price']]
    model = KMeans(n_clusters=3, random_state=42, n_init='auto')
    df['price_cluster'] = model.fit_predict(X)
    return df

def summary_by_cluster(df):
    return df.groupby('price_cluster')['price'].describe()

def plot_price_clusters(df):
    plt.scatter(df.index, df['price'], c=df['price_cluster'], cmap='viridis')
    plt.title("Clustering des jeux par prix")
    plt.xlabel("Index")
    plt.ylabel("Prix (€)")
    plt.savefig("data/clustering_games.png")
    plt.close()

def plot_cluster_distribution(df):
    df.boxplot(column='price', by='price_cluster')
    plt.title("Distribution des prix par cluster")
    plt.suptitle("")
    plt.xlabel("Cluster")
    plt.ylabel("Prix (€)")
    plt.savefig("data/cluster_boxplot_games.png")
    plt.close()
