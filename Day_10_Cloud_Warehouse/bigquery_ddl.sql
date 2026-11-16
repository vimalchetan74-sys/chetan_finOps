-- BigQuery example. Replace project.dataset with your own identifiers.
CREATE TABLE IF NOT EXISTS `project.dataset.billing_usage`
(
  usage_date DATE,
  account_id STRING,
  resource_id STRING,
  service STRING,
  region STRING,
  environment STRING,
  usage_quantity FLOAT64,
  cost_usd NUMERIC
)
PARTITION BY usage_date
CLUSTER BY account_id, service, region
OPTIONS(description="Normalized cloud billing usage and cost");
