"""
Package `src` pour le projet FUTURE_DS_02.
Contient des modules réutilisables pour le nettoyage, le chargement et la visualisation des données.
"""

# Import des fonctions depuis les modules pour un accès direct
from src.data_cleaning import (
    clean_missing_values,
    clean_total_charges,
    convert_churn_to_binary,
    add_derived_columns,
)

from src.data_loading import load_data

from src.visualization import (
    plot_churn_distribution,
    plot_tenure_distribution,
)

from src.utils import setup_logger, ensure_directory_exists

# Définition de ce qui est accessible depuis le package
__all__ = [
    # Fonctions de nettoyage
    "clean_missing_values",
    "clean_total_charges",
    "convert_churn_to_binary",
    "add_derived_columns",

    # Fonctions de chargement
    "load_data",

    # Fonctions de visualisation
    "plot_churn_distribution",
    "plot_tenure_distribution",

    # Utilitaires
    "setup_logger",
    "ensure_directory_exists",

    # Fonctions d'analyse de churn
    "calculate_retention_rate_by_tenure",
    "calculate_ltv",
    "get_cohort_retention",
    "get_ltv_by_segment",
]