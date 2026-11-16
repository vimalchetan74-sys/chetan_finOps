import pandas as pd
from pathlib import Path

src = pd.read_csv("Datasets/raw_billing.csv")
required = ["usage_date","account_id","resource_id","service","usage_quantity","cost_usd"]
missing_cols = [c for c in required if c not in src.columns]
bad = pd.DataFrame()
if not missing_cols:
    numeric = src.copy()
    numeric["cost_usd"] = pd.to_numeric(numeric["cost_usd"], errors="coerce")
    numeric["usage_quantity"] = pd.to_numeric(numeric["usage_quantity"], errors="coerce")
    invalid = numeric[required].isna().any(axis=1) | numeric["cost_usd"].lt(0) | numeric["usage_quantity"].lt(0)
    duplicates = numeric.duplicated(subset=["usage_date","account_id","resource_id","service"], keep=False)
    bad = numeric[invalid | duplicates].copy()
    bad["quarantine_reason"] = "invalid_or_duplicate_review"
Path("Day_06_Data_Quality/output").mkdir(parents=True, exist_ok=True)
bad.to_csv("Day_06_Data_Quality/output/quarantine.csv", index=False)
report = {
    "input_rows": len(src), "missing_columns": missing_cols,
    "quarantine_rows": len(bad), "null_cells": int(src.isna().sum().sum())
}
pd.Series(report).to_csv("Day_06_Data_Quality/output/quality_report.csv", header=["value"])
print(report)
