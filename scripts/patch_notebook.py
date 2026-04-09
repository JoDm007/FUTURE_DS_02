import json
import sys

path = r"e:\Certifs\Future_Interns\FUTURE_DS_02\notebooks\01_data_cleaning.ipynb"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("looger = setup_logger", "logger = setup_logger")
text = text.replace("convert_churn_to_binary\\n\",", "convert_churn_to_binary, add_derived_columns\\n\",")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Notebook patched successfully.")
