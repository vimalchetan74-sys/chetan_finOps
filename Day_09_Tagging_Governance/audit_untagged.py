import pandas as pd
required = ["owner","team","environment"]
df = pd.read_csv("Datasets/asset_inventory.csv").fillna("")
mask = df[required].eq("").any(axis=1) | df["status"].eq("orphaned")
out = df.loc[mask].copy()
out["audit_issue"] = out.apply(
    lambda r: "orphaned_resource" if r["status"] == "orphaned" else "missing_required_tag", axis=1)
out.to_csv("Day_09_Tagging_Governance/untagged_resources.csv", index=False)
print(f"Flagged {len(out)} resources")
