import pandas as pd
assets = pd.DataFrame([
    {"asset":"Compute server","capitalized_cost":12000,"useful_life_months":36,"in_service_month":"2026-01"},
    {"asset":"Software development","capitalized_cost":24000,"useful_life_months":24,"in_service_month":"2026-01"},
])
assets["monthly_depreciation"] = assets["capitalized_cost"] / assets["useful_life_months"]
assets.to_csv("Day_16_Amortization/amortization_schedule.csv",index=False)
print(assets.to_string(index=False))
