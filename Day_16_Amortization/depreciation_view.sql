-- SQLite-style straight-line monthly charge view over an illustrative asset table.
CREATE VIEW IF NOT EXISTS vw_monthly_asset_depreciation AS
SELECT asset_id, asset_name,
       capitalized_cost / useful_life_months AS monthly_depreciation
FROM assets
WHERE useful_life_months > 0;
