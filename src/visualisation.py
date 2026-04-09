#Autor: Joseph DATE-MASSE

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path

def save_plot(filename: str):
    """Sauvegarde le graphique actuel dans reports/images."""
    # Le fichier est dans src/, donc parent.parent est la racine du projet
    save_dir = Path(__file__).resolve().parent.parent / "reports" / "images"
    save_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(save_dir / filename, bbox_inches='tight', dpi=300)
    print(f"Graphique sauvegardé dans : {save_dir / filename}")

# Configuration du style par défaut pour de beaux graphiques
sns.set_theme(style="whitegrid", palette="muted")

def plot_churn_distribution(df: pd.DataFrame):
    """Affiche la distribution globale du Churn."""
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(x='Churn', data=df)
    plt.title("Distribution du Churn (0 = No, 1 = Yes)", fontsize=14, fontweight='bold')
    
    # Ajout des pourcentages
    total = len(df)
    for p in ax.patches:
        percentage = f'{100 * p.get_height() / total:.1f}%'
        x = p.get_x() + p.get_width() / 2 - 0.05
        y = p.get_height() + 50
        ax.annotate(percentage, (x, y), ha='center', fontsize=12)
        
    save_plot("churn_distribution.png")
    plt.show()

def plot_tenure_distribution(df: pd.DataFrame):
    """Affiche la distribution de la durée d'abonnement (tenure)."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['tenure'], bins=30, kde=True, color='teal')
    plt.title("Distribution de l'Ancienneté (Tenure en mois)", fontsize=14, fontweight='bold')
    plt.xlabel("Mois d'abonnement")
    plt.ylabel("Nombre de clients")
    save_plot("tenure_distribution.png")
    plt.show()

def plot_churn_by_category(df: pd.DataFrame, category_col: str):
    """Affiche le taux de désabonnement pour une variable catégorielle."""
    plt.figure(figsize=(8, 5))
    
    # Calcul du taux de churn
    churn_rate = df.groupby(category_col)['Churn'].mean().reset_index()
    
    ax = sns.barplot(x=category_col, y='Churn', data=churn_rate, palette="coolwarm", hue=category_col, legend=False)
    plt.title(f"Taux de Churn selon : {category_col}", fontsize=14, fontweight='bold')
    plt.ylabel("Taux de Churn (%)")
    plt.xlabel(category_col)
    
    # Formatage de l'axe y en pourcentage
    ticks = ax.get_yticks()
    ax.set_yticks(ticks)
    ax.set_yticklabels([f"{int(y*100)}%" for y in ticks])
    
    # Ajout des valeurs
    for p in ax.patches:
        percentage = f'{p.get_height()*100:.1f}%'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height() + 0.01
        ax.annotate(percentage, (x, y), ha='center', fontsize=11)
        
    plt.xticks(rotation=45 if df[category_col].nunique() > 4 else 0)
    plt.tight_layout()
    # Nettoyer les caractères spéciaux pour le nom de fichier
    safe_col_name = "".join([c if c.isalnum() else "_" for c in category_col])
    save_plot(f"churn_by_{safe_col_name}.png")
    plt.show()

def plot_numeric_distributions_by_churn(df: pd.DataFrame, numeric_col: str):
    """Affiche un boxplot pour observer la distribution d'une valeur numérique selon le churn."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Churn', y=numeric_col, data=df, palette="coolwarm", hue='Churn', legend=False)
    plt.title(f"Distribution de {numeric_col} selon le Churn", fontsize=14, fontweight='bold')
    plt.xlabel("Churn (0 = No, 1 = Yes)")
    plt.ylabel(numeric_col)
    safe_col_name = "".join([c if c.isalnum() else "_" for c in numeric_col])
    save_plot(f"numeric_dist_{safe_col_name}.png")
    plt.show()

def plot_correlation_matrix(df: pd.DataFrame):
    """Identifie et affiche les corrélations entre les variables numériques."""
    num_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(10, 8))
    
    matrix = np.triu(num_df.corr())
    sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap="vlag", center=0, mask=matrix)
    plt.title("Matrice de Corrélation", fontsize=14, fontweight='bold')
    save_plot("correlation_matrix.png")
    plt.show()