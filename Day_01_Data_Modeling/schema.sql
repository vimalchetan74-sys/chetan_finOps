PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS dim_account (
  account_key INTEGER PRIMARY KEY, account_id TEXT NOT NULL UNIQUE, account_name TEXT
);
CREATE TABLE IF NOT EXISTS dim_resource (
  resource_key INTEGER PRIMARY KEY, resource_id TEXT NOT NULL UNIQUE, resource_type TEXT,
  service TEXT, environment TEXT
);
CREATE TABLE IF NOT EXISTS dim_region (
  region_key INTEGER PRIMARY KEY, region_name TEXT NOT NULL UNIQUE, cloud_provider TEXT
);
CREATE TABLE IF NOT EXISTS dim_tag (
  tag_key INTEGER PRIMARY KEY, tag_name TEXT NOT NULL, tag_value TEXT NOT NULL,
  UNIQUE(tag_name, tag_value)
);
CREATE TABLE IF NOT EXISTS dim_date (
  date_key INTEGER PRIMARY KEY, full_date TEXT NOT NULL UNIQUE, year INTEGER, month INTEGER, day INTEGER
);
CREATE TABLE IF NOT EXISTS fact_usage_cost (
  usage_key INTEGER PRIMARY KEY, date_key INTEGER NOT NULL, account_key INTEGER NOT NULL,
  resource_key INTEGER NOT NULL, region_key INTEGER NOT NULL, tag_key INTEGER,
  usage_quantity REAL NOT NULL, cost_usd REAL NOT NULL,
  FOREIGN KEY(date_key) REFERENCES dim_date(date_key),
  FOREIGN KEY(account_key) REFERENCES dim_account(account_key),
  FOREIGN KEY(resource_key) REFERENCES dim_resource(resource_key),
  FOREIGN KEY(region_key) REFERENCES dim_region(region_key),
  FOREIGN KEY(tag_key) REFERENCES dim_tag(tag_key)
);
CREATE INDEX IF NOT EXISTS idx_fact_date_account ON fact_usage_cost(date_key, account_key);
CREATE INDEX IF NOT EXISTS idx_fact_resource ON fact_usage_cost(resource_key);
