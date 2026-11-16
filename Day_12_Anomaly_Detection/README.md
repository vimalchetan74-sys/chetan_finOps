# Day 12 — Real-time Cloud Anomaly Detection
Run `python Day_12_Anomaly_Detection/anomaly_engine.py --input Datasets/daily_costs.csv`. This is a batch demonstration using a rolling seven-observation z-score threshold. For production, account for seasonality, minimum history, robust statistics, alert deduplication and webhook secret management. No webhook is sent by this sample.
