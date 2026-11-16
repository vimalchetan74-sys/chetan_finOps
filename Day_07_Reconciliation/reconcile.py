import pandas as pd
from pathlib import Path
src = pd.read_csv("Datasets/raw_billing.csv")
clean_path = Path("Day_03_Python_ETL/output/clean_billing.csv")
if not clean_path.exists():
    raise SystemExit("Run Day 3 ETL first.")
tgt = pd.read_csv(clean_path)
src_total = pd.to_numeric(src["cost_usd"], errors="coerce").sum()
tgt_total = pd.to_numeric(tgt["cost_usd"], errors="coerce").sum()
report = pd.DataFrame([
    ["source_rows",len(src)],["target_rows",len(tgt)],
    ["source_cost_usd",round(src_total,2)],["target_cost_usd",round(tgt_total,2)],
    ["row_delta",len(src)-len(tgt)],["cost_delta_usd",round(src_total-tgt_total,2)]
],columns=["metric","value"])
Path("Day_07_Reconciliation/output").mkdir(parents=True,exist_ok=True)
report.to_csv("Day_07_Reconciliation/output/reconciliation.csv",index=False)
print(report.to_string(index=False))
