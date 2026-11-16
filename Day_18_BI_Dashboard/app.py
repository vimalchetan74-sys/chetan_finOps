import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title="PACEX FinOps Dashboard", layout="wide")
st.title("Cloud Financial Intelligence — Demo")
st.caption("Synthetic demonstration data. Not connected to a live cloud billing account.")
df = pd.read_csv(Path(__file__).resolve().parents[1] / "Datasets" / "daily_costs.csv", parse_dates=["date"])
total = df["cost_usd"].sum()
avg = df["cost_usd"].mean()
peak = df.loc[df["cost_usd"].idxmax()]
a,b,c = st.columns(3)
a.metric("Total spend", f"${total:,.2f}")
b.metric("Average daily spend", f"${avg:,.2f}")
c.metric("Peak day", f"${peak['cost_usd']:,.2f}", str(peak["date"].date()))
st.line_chart(df.set_index("date")["cost_usd"])
st.dataframe(df, use_container_width=True)
