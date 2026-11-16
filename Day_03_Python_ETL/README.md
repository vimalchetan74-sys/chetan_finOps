# Day 3 — Python Data Ingestion & Cleansing
Run:
`python Day_03_Python_ETL/ingest_billing.py --input Datasets/raw_billing.csv --output Day_03_Python_ETL/output/clean_billing.csv`

The script parses dates, coerces numeric columns, fills selected missing dimensions, removes invalid metric rows and duplicates. Review the output and record row counts before/after. Do not silently discard bad records in a production pipeline; route them to quarantine with a reason.
