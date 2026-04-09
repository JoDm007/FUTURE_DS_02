import sys
from pathlib import Path

project_root = Path.cwd()
if project_root.name == "notebooks":
    project_root = project_root.parent

sys.path.append(str(project_root / "src"))

from utils import setup_logger, ensure_directory_exists
from data_loading import load_data
from data_cleaning import clean_missing_values, clean_total_charges, convert_churn_to_binary, add_derived_columns
from visualization import plot_churn_distribution, plot_tenure_distribution

logger = setup_logger("../reports/logs/data_cleaning.log")

INPUT_PATH = str(project_root / "data/raw/WA_Fn_Use_C_Telco_Customer_Churn.csv")
OUTPUT_PATH = str(project_root / "data/processed/churn_cleaned.csv")

print("Loading data...")
try:
    df = load_data(INPUT_PATH)
except Exception as e:
    print("Error loading:", e)

try:
    df = clean_missing_values(df)
    df = clean_total_charges(df)
    df = convert_churn_to_binary(df)
    df = add_derived_columns(df)
except Exception as e:
    print("Error cleaning:", e)

try:
    ensure_directory_exists(str(Path(OUTPUT_PATH).parent))
    df.to_csv(OUTPUT_PATH, index=False)
except Exception as e:
    print("Error saving:", e)
