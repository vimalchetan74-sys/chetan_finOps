-- Day 2: eight analytical queries. Run against the demo schema after loading data.
-- Assumes a flattened billing table named billing_usage for portability.
-- Create it using: scripts/load_demo_db.py

-- Q1 Daily spend
SELECT usage_date, ROUND(SUM(cost_usd),2) AS daily_cost
FROM billing_usage GROUP BY usage_date ORDER BY usage_date;

-- Q2 Rank resources by spend within each day
SELECT usage_date, resource_id, SUM(cost_usd) AS cost,
       RANK() OVER (PARTITION BY usage_date ORDER BY SUM(cost_usd) DESC) AS spend_rank
FROM billing_usage GROUP BY usage_date, resource_id;

-- Q3 Day-over-day cost change using LAG
WITH daily AS (
  SELECT usage_date, SUM(cost_usd) AS cost
  FROM billing_usage GROUP BY usage_date
)
SELECT usage_date, cost,
       LAG(cost) OVER (ORDER BY usage_date) AS previous_day_cost,
       cost - LAG(cost) OVER (ORDER BY usage_date) AS change_usd
FROM daily ORDER BY usage_date;

-- Q4 Running cumulative spend
WITH daily AS (
  SELECT usage_date, SUM(cost_usd) AS cost
  FROM billing_usage GROUP BY usage_date
)
SELECT usage_date, cost,
       SUM(cost) OVER (ORDER BY usage_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_cost
FROM daily;

-- Q5 Service and environment aggregation
SELECT service, environment, ROUND(SUM(cost_usd),2) AS spend
FROM billing_usage GROUP BY service, environment ORDER BY spend DESC;

-- Q6 Top three resources by total spend
WITH totals AS (
  SELECT resource_id, SUM(cost_usd) AS spend FROM billing_usage GROUP BY resource_id
), ranked AS (
  SELECT *, DENSE_RANK() OVER (ORDER BY spend DESC) AS rnk FROM totals
)
SELECT resource_id, ROUND(spend,2) AS spend FROM ranked WHERE rnk <= 3;

-- Q7 Seven-row rolling average daily spend
WITH daily AS (
  SELECT usage_date, SUM(cost_usd) AS cost FROM billing_usage GROUP BY usage_date
)
SELECT usage_date, cost,
       AVG(cost) OVER (ORDER BY usage_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7_day_avg
FROM daily;

-- Q8 CTE: high-cost resources above the overall average resource cost
WITH resource_cost AS (
  SELECT resource_id, SUM(cost_usd) AS spend FROM billing_usage GROUP BY resource_id
), avg_cost AS (
  SELECT AVG(spend) AS avg_spend FROM resource_cost
)
SELECT r.resource_id, ROUND(r.spend,2) AS spend
FROM resource_cost r CROSS JOIN avg_cost a
WHERE r.spend > a.avg_spend ORDER BY r.spend DESC;
