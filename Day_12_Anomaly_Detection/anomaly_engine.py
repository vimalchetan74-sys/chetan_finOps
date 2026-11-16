import argparse
import pandas as pd

def detect(path):
    df = pd.read_csv(path, parse_dates=["date"]).sort_values("date")
    df["rolling_mean"] = df["cost_usd"].rolling(7, min_periods=4).mean()
    df["rolling_std"] = df["cost_usd"].rolling(7, min_periods=4).std().fillna(0)
    df["z_score"] = (df["cost_usd"] - df["rolling_mean"]) / df["rolling_std"].replace(0, pd.NA)
    df["is_anomaly"] = df["z_score"].abs() >= 2.0
    return df

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); args=ap.parse_args()
    result=detect(args.input)
    print(result[result["is_anomaly"]].to_string(index=False))
    result.to_csv("Day_12_Anomaly_Detection/anomaly_results.csv",index=False)
