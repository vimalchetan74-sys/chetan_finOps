import sqlite3, pandas as pd
from pathlib import Path
root=Path(__file__).resolve().parents[1]
df=pd.read_csv(root/"Datasets"/"raw_billing.csv")
con=sqlite3.connect(root/"Datasets"/"demo.db")
df.to_sql("billing_usage",con,if_exists="replace",index=False)
print("Loaded",len(df),"rows into Datasets/demo.db table billing_usage")
con.close()
