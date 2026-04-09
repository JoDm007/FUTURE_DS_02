# Telecom Churn & Customer Retention Analysis Project

## Project Structure

This project analyzes customer data for a subscription-based business to identify churn patterns, key retention drivers, and customer lifetime trends.

### Directory Structure

```
FUTURE_DS_02/
├── data/
│   ├── raw/                     # Original datasets
│   │   └── WA_Fn_Use_C_Telco_Customer_Churn.csv
│   └── processed/               # Cleaned and processed data
│       └── churn_cleaned.csv
│
├── notebooks/                   # Jupyter notebooks for analysis
│   ├── 01_data_cleaning.ipynb          # Data cleaning and preprocessing
│   ├── 02_exploratory_analysis.ipynb   # EDA and visualizations
│   └── 03_churn_analysis_metrics.ipynb # Cohort & retention metrics calculation
│
├── reports/                     # Final reports and logs
│   ├── logs/
│   └── images/                  # Generated charts and graphs
│
├── tableau/                     # Power BI / Tableau dashboards
│
├── src/                         # Reusable Python scripts
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── utils.py
│   ├── visualisation.py
│   ├── metrics.py
│   └── churn_analysis_functions.py
│
├── F_DS_02_env/                 # Virtual Environment
├── README.md
└── requirements.txt
```

## Analysis Objectives

1. **Churn Patterns**: Analyze customer demographics and account information to identify factors leading to churn.
2. **Retention Drivers**: Determine which services, contract types, or payment methods keep customers subscribed.
3. **Cohort & Retention Analysis**: Analyze customer drop-off points across different tenure groups.
4. **Customer Lifetime Trends**: Calculate Customer Lifetime Value (LTV) and survival rates.

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Run the notebooks in order: 01 → 02 → 03
3. View final visualizations and data exports prepared for your Power BI dashboard.

## 👤 Auteur
Joseph DATE-MASSE - Intern Data Science & Analytics @ Future Interns
