# Projet Analyse de Rétention et Churn (Telecom)

Ce plan décrit les étapes pour mener à bien l'analyse de rétention client et la préparation des données pour votre tableau de bord Power BI ou Excel.

## Objectif

Compléter le nettoyage des données, effectuer une exploration ciblée sur les facteurs de churn, calculer des métriques avancées (analyse de cohorte, LTV, courbes de survie), et exporter des agrégations propres pour la création d'un dashboard.

## Modifications Proposées

---

### Phase 1 : Finalisation du nettoyage des données (Data Cleaning)

Il manque un import dans votre notebook qui empêche la complétion de l'étape de nettoyage.

#### [MODIFY] [01_data_cleaning.ipynb](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/notebooks/01_data_cleaning.ipynb)
- Ajouter l'import de `add_derived_columns` depuis `src.data_cleaning`.
- Exécuter et sauvegarder le dataset final dans `data/processed/churn_cleaned.csv`.

---

### Phase 2 : Analyse Exploratoire des Données (EDA)

Nous allons déplacer la logique visuelle dans le code source et l'utiliser dans le 2e notebook.

#### [MODIFY] [visualisation.py](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/src/visualisation.py)
- Ajouter de nouvelles fonctions de visualisation (ex: `plot_churn_by_category` pour Contract, PaymentMethod, etc.).
- Ajouter `plot_numeric_distributions_by_churn` pour MonthlyCharges et TotalCharges.

#### [MODIFY] [02_exploratory_analysis.ipynb](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/notebooks/02_exploratory_analysis.ipynb)
- Import des fonctions depuis `src/visualisation.py`.
- Analyse bivariée pour identifier les facteurs de désabonnement les plus importants.

---

### Phase 3 : Métriques de Churn, Analyse de Rétention & Cohorte

Nous allons analyser le taux de rétention sur la durée de vie du client.

#### [MODIFY] [churn_analysis_functions.py](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/src/churn_analysis_functions.py)
- Création d'une fonction `calculate_retention_rate_by_tenure` pour modéliser une courbe de survie (rétention).
- Création d'une fonction `calculate_ltv` (Customer Lifetime Value) basée sur l'ARPU et la durée de vie moyenne.

#### [MODIFY] [03_churn_analysis_metrics.ipynb](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/notebooks/03_churn_analysis_metrics.ipynb)
- Application de ces métriques.
- Création d'agrégations prêtes pour le reporting.

---

### Phase 4 : Export pour le Dashboard Power BI / Excel

#### [NEW] [export_dashboard_data.py](file:///e:/Certifs/Future_Interns/FUTURE_DS_02/scripts/export_dashboard_data.py) (Optionnel)
- Génération de fichiers CSV spécifiques et agrégés dans `data/processed/` (ex: `cohort_retention.csv`, `churn_factors_summary.csv`) pour faciliter la connexion avec Power BI ou Tableau.

## Questions Ouvertes

> [!IMPORTANT]
> - Dans Power BI, préférez-vous importer le gros fichier complet `churn_cleaned.csv` pour faire vos visualisations, ou souhaitez-vous que je génère via Python des fichiers agrégés qui seront plus légers ?
> - Avez-vous besoin que je structure d'une certaine manière les analyses de cohorte (étant donné qu'on a la variable "tenure" en mois mais pas la date de souscription exacte) ?

## Plan de Validation

### Vérification Manuelle
- S'assurer que le fichier `churn_cleaned.csv` est correctement créé.
- Les notebooks 2 et 3 s'exécutent sans erreurs.
- Les données exportées pour Power BI / Excel correspondent aux recommandations exploitables attendues dans l'énoncé de la tâche.
