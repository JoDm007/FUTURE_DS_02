#Autor: Joseph DATE-MASSE

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
    """Ajoute des colonnes dérivées (tenure_group)."""
    logger.info("|==> Ajout des colonnes dérivées...")
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[-1, 6, 12, 24, 36, 48, 60, 72],
        labels=['0-6 mois', '6-12 mois', '1-2 ans', '2-3 ans', '3-4 ans', '4-5 ans', '5-6 ans']
    )
    return df