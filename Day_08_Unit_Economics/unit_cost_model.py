# Example unit economics. Replace denominators with measured business telemetry.
monthly_cloud_cost_usd = 12500.0
api_requests = 2_500_000
active_customers = 12500
processing_hours = 800
metrics = {
    "cost_per_api_request_usd": monthly_cloud_cost_usd / api_requests,
    "cost_per_active_customer_usd": monthly_cloud_cost_usd / active_customers,
    "compute_cost_per_processing_hour_usd": monthly_cloud_cost_usd / processing_hours,
}
for name, value in metrics.items():
    print(f"{name}: {value:.6f}")
