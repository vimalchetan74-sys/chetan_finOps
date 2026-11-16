import argparse
from pathlib import Path
import pandas as pd

REQUIRED = ["usage_date", "account_id", "resource_id", "service", "region", "usage_quantity", "cost_usd"]

def transform(input_path: str, output_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    for col in REQUIRED:
        if col not in df.columns:
            df[col] = pd.NA
    df["usage_date"] = pd.to_datetime(df["usage_date"], errors="coerce").dt.strftime("%Y-%m-%d")
    for col in ["usage_quantity", "cost_usd"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["environment"] = df.get("environment", pd.Series(index=df.index, dtype="object")).fillna("unknown")
    df["region"] = df["region"].fillna("unknown")
    df["account_id"] = df["account_id"].fillna("unknown")
    df["resource_id"] = df["resource_id"].fillna("unknown")
    df = df.dropna(subset=["usage_date", "usage_quantity", "cost_usd"])
    df = df.drop_duplicates()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    result = transform(args.input, args.output)
    print(f"Rows written: {len(result)}")
    print(f"Output: {args.output}")
