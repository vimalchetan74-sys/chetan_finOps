import pandas as pd
df=pd.read_csv("Day_13_Kubernetes_Cost/kubecost_analysis.csv")
df["cpu_request_utilization_pct"]=df["cpu_actual_cores"]/df["cpu_request_cores"]*100
df["memory_request_utilization_pct"]=df["memory_actual_gib"]/df["memory_request_gib"]*100
df["cpu_overprovisioned"]=df["cpu_request_utilization_pct"]<40
df["memory_overprovisioned"]=df["memory_request_utilization_pct"]<40
df.to_csv("Day_13_Kubernetes_Cost/resource_efficiency_report.csv",index=False)
print(df.to_string(index=False))
