import pandas as pd
from pathlib import Path
df = pd.read_csv("Datasets/raw_billing.csv")
df["cost_usd"] = pd.to_numeric(df["cost_usd"], errors="coerce")
df["usage_quantity"] = pd.to_numeric(df["usage_quantity"], errors="coerce")
df["service"] = df["service"].fillna("Unknown")
summary = df.groupby("service", dropna=False).agg(
    total_cost_usd=("cost_usd","sum"), usage_total=("usage_quantity","sum"),
    row_count=("service","size")).reset_index()
summary["cost_share_pct"] = summary["total_cost_usd"] / summary["total_cost_usd"].sum() * 100
Path("Day_04_Cloud_Billing/output").mkdir(parents=True, exist_ok=True)
summary.to_csv("Day_04_Cloud_Billing/output/service_cost_profile.csv", index=False)
print(summary.to_string(index=False))
