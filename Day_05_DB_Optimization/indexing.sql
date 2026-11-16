-- Baseline query
EXPLAIN QUERY PLAN
SELECT account_id, SUM(cost_usd)
FROM billing_usage
WHERE usage_date >= '2026-10-01' AND usage_date < '2026-11-01'
GROUP BY account_id;

-- Index candidates
CREATE INDEX IF NOT EXISTS idx_billing_date ON billing_usage(usage_date);
CREATE INDEX IF NOT EXISTS idx_billing_account_date ON billing_usage(account_id, usage_date);
CREATE INDEX IF NOT EXISTS idx_billing_service_region ON billing_usage(service, region);

-- Re-run EXPLAIN QUERY PLAN after creating indexes and compare the plan.
-- PostgreSQL users: use EXPLAIN (ANALYZE, BUFFERS) and record actual execution time.
