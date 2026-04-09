# 📑 Rapport Final : Analyse de Rétention et de Churn Client

**Projet :** Telecom Customer Churn & Retention Analysis  
**Auteur :** Joseph DATE-MASSE - Intern Data Science & Analytics @ Future Interns  
**Date :** Avril 2026

---

## 1. Objectifs de l'Analyse
Ce projet a été mené pour une entreprise confrontée à une attrition (churn) de sa clientèle. L'objectif était d'analyser les données historiques des abonnés afin de :
- Identifier les profils et segments les plus susceptibles de résilier.
- Comprendre les moteurs d'attrition (pourquoi les clients partent).
- Mesurer la valeur financière des clients (LTV) et les taux de rétention par cohortes.
- Proposer des recommandations stratégiques actionnables.

---

## 2. Méthodologie et Préparation des Données (Data Cleaning)
Avant toute modélisation, une rigoureuse ingénierie des données a été réalisée via nos modules métier locaux (`src/data_cleaning.py` et `src/data_loading.py`).

**Étapes clés de la préparation :**
1. **Typage des données :** La variable financière `TotalCharges` comportait des espaces vides pour les tout nouveaux clients, empêchant les calculs mathématiques. Nous l'avons convertie de Texte vers Décimal et avons épuré ces clients "fantômes".
2. **Binarisation de la cible :** La cible principale `Churn` (Yes/No) a été encodée en binaire `(1/0)`. C'est une manipulation mathématique forte qui permet par la suite d'obtenir le Taux de Churn d'un segment par un simple calcul de moyenne.
3. **Ingénierie de Caractéristiques (Feature Engineering) :** Création d'une variable `tenure_group`. L'ancienneté en mois (allant de 0 à 72) a été agglomérée en "Cohortes d'ancienneté" (ex: *0-6 mois, 6-12 mois, 1-2 ans*) pour dégager des schémas de cycle de vie au lieu d'un simple nuage de points.

---

## 3. Analyse Exploratoire (Découverte des leviers d'attrition)

*(Nous avons encapsulé la lourde logique graphique via `seaborn` et `matplotlib` dans `src/visualisation.py` pour un rendu automatisé et hautement professionnel).*

### A. Le Constat de base
L'analyse globale a révélé un **Taux de Churn global d'environ 26.5%**. C'est un taux particulièrement alarmant pour un business modèle à souscription régulier (SaaS/Telecom), suggérant une crise majeure de fidélisation ou d'insatisfaction.

### B. Le Piège du "Sans Engagement"
L'analyse par cohorte de contrats (`Contract`) a révélé l'information prédictive la plus claire du dataset :
- Les abonnements mensuels (*Month-to-Month*) voient près de **42% de leurs clients partir**.
- Les contrats d'un an ont un churn de **11%**.
- Les contrats de deux ans tombent à un exceptionnel **3%**.
**Insight :** Le non-engagement contractuel est le pire ennemi de l'entreprise.

### C. Le Profil Premium est paradoxalement volatil
L'analyse des Variables Financières (boxplot sur `MonthlyCharges`) a prouvé de façon contre-intuitive que :
- Les clients qui partent paient une facture mensuelle médiane plus élevée que ceux qui restent.
- La matrice de corrélation montre que plus le prix augmente, plus le risque départ augmente (corrélation positive avec le Churn). Associé au fait curieux que la Fibre Optique enregistre plus de départs que l'ADSL traditionnel.
**Insight :** L'offre très haut-débit et chère souffre d'un mauvais alignement Qualité/Prix dans l'esprit du consommateur.

---

## 4. Cohortes, Rétention & Valeur à Vie (LTV)

*(Calculs exécutés via la logique de `src/metrics.py` et `src/churn_analysis_functions.py`)*

### A. La Période Critique (Analyse de survie / Rétention)
La création de notre table de rétention par ancienneté a mis en exergue "l'effet de falaise" initial. 
* Près de 50% de nos désabonnements ont lieu **au cours des 6 premiers mois**. 
* Si un usager "survit" à la première année, et à fortiori aux deux premières années (où la rétention grimpe au-delà de 90%), sa fidélité est quasiment garantie.

### B. La Customer Lifetime Value (LTV)
La LTV (calculée mathématiquement par la formule : `Revenu Moyen (ARPU) / Taux de Churn`) offre l'argument financier final :
- Le client mensuel a certes un revenu fort immédiat, mais son churn de 42% détruit sa "Valeur Totale" pour l'entreprise.
- Le client engagé sur deux ans a potentiellement bénéficié de réductions (ARPU inférieur), mais avec un churn de 3%, sa Valeur à Vie (LTV) est **plusieurs fois supérieure** à un client standard.

---

## 5. Recommandations et Plan d'Action Stratégique

Toutes ces analyses chiffrées n'ont de valeur que si elles se traduisent par des décisions d'entreprise. Si j'étais face au comité de direction, voici les 3 piliers stratégiques que je défendrais :

1. **Pousser massivement la bascule vers les Contrats Annuels :**
   Il est financièrement rentable (au vu des calculs de la LTV croisée) d'offrir des mois gratuits (ex: payer 10 mois au lieu de 12), des réductions matérielles, ou même Netflix offert, *POURVU* que le client s'engage sur un an au lieu de rester au mois le mois. L'amortissement financier de cet investissement est garanti.

2. **Mettre en place un plan "Soins Intensifs" des Nouveaux (Onboarding) :**
   La majorité du churn s'opérant dans le premier semestre, il faut allouer l'intégralité du budget du service fidélisation (appels de courtoisie, aide technique proactive, relances, cadeaux de bienvenue) concentré sur le **0 à 6ème mois** de vie du contrat.

3. **Favoriser et inciter l'encaissement automatique :**
   Les graphiques de méthode de paiement ayant prouvé que l'envoi de chèque manuel était un vecteur massif de churn, l'inscription devrait privilégier l'ajout automatique de prélèvement bancaire lors de la transaction.



