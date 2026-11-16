# Illustrative rate comparison. Actual discounts vary by provider, region, term and utilization.
workload_hours = 730
ondemand_hourly = 0.80
options = {
    "On-Demand": 1.00,
    "1-year commitment": 0.72,
    "3-year commitment": 0.58,
    "Spot (effective blended)": 0.35,
}
baseline = workload_hours * ondemand_hourly
print(f"On-Demand monthly: ${baseline:,.2f}")
for name, multiplier in options.items():
    spend = baseline * multiplier
    savings = (baseline - spend) / baseline * 100
    print(f"{name}: ${spend:,.2f}; savings {savings:.1f}%")
