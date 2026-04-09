import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_churn_distribution(df: pd.DataFrame):
    """Affiche la distribution du Churn."""
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Churn', data=df)
    plt.title("Distribution du Churn")
    plt.show()

def plot_tenure_distribution(df: pd.DataFrame):
    """Affiche la distribution de la durée d'abonnement (tenure)."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['tenure'], bins=20, kde=True)
    plt.title("Distribution de la durée d'abonnement (tenure)")
    plt.show()