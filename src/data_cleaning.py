import pandas as pd
import numpy as np
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les lignes avec des valeurs manquantes."""
    logger.info("|==> Nettoyage des valeurs manquantes...")
    return df.dropna()

def clean_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie la colonne TotalCharges."""
    logger.info("|==> Nettoyage de TotalCharges...")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df.dropna(subset=["TotalCharges"])

def convert_churn_to_binary(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit la colonne Churn en valeurs binaires."""
    logger.info("|==> Conversion du Churn en binaire...")
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute des colonnes dérivées (ex: tenure_group)."""
    logger.info("|==> Ajout des colonnes dérivées...")
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[-1, 12, 24, 48, 72, np.inf],
        labels=['0-12 mois', '12-24 mois', '24-48 mois', '48-72 mois', '72+ mois']
    )
    return df