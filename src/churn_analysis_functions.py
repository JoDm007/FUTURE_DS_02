#Autor: Joseph DATE-MASSE

import pandas as pd
from metrics import calculate_ltv

def get_cohort_retention(df: pd.DataFrame, group_col: str = 'tenure_group') -> pd.DataFrame:
    """
    Crée une table de cohorte ou par segment montrant le taux de rétention brut.
    Très utile pour voir comment le désabonnement évolue selon l'ancienneté.
    """
    cohort = df.groupby(group_col).agg(
        total_customers=('Churn', 'count'),
        churned=('Churn', 'sum')
    ).reset_index()
    
    # Le pourcentage de personnes qui restent
    cohort['retention_rate_%'] = ((1 - (cohort['churned'] / cohort['total_customers'])) * 100).round(2)
    return cohort

def get_ltv_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """
    Calcule la LTV (Customer Lifetime Value) pour n'importe quel segment.
    Cela permet de savoir "Qui nous rapporte le plus d'argent sur le long terme ?".
    """
    segment_stats = df.groupby(segment_col).agg(
        arpu=('MonthlyCharges', 'mean'),       # Dépense moyenne par mois
        churn_rate=('Churn', 'mean'),          # Probabilité de départ
        total_clients=('Churn', 'count')
    ).reset_index()
    
    # Application de la formule mathématique du fichier metrics.py
    segment_stats['LTV_Estimee_$'] = segment_stats.apply(
        lambda row: calculate_ltv(row['arpu'], row['churn_rate']),
        axis=1
    ).round(2)
    
    # On trie pour mettre les meilleurs clients en haut
    return segment_stats.sort_values(by="LTV_Estimee_$", ascending=False)
