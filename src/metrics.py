#Autor: Joseph DATE-MASSE

def calculate_ltv(arpu: float, churn_rate: float) -> float:
    """
    Calcule la Customer Lifetime Value (LTV) globale.
    Formule standard en SaaS/Telecom : LTV = ARPU / Taux de Churn.
    """
    if churn_rate == 0:
        return float('inf')
    return arpu / churn_rate

def calculate_retention_rate(total_customers: int, churned_customers: int) -> float:
    """Calcule le taux de rétention basique."""
    if total_customers == 0:
        return 0.0
    return 1 - (churned_customers / total_customers)
