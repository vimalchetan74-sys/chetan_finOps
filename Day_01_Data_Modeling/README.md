# Day 1 — Enterprise Data Modeling & Dimensional Design
**Task:** Design a dimensional star schema for cloud usage telemetry and billing data.

**Deliverables:** `schema.sql` creates fact and dimension tables, primary keys, foreign keys and indexes. `erd.mmd` is a Mermaid ER diagram source.

**Run:** `python ../../scripts/run_sqlite.py schema.sql` from this folder, or `python scripts/run_sqlite.py Day_01_Data_Modeling/schema.sql` from repository root.

**Validate:** Inspect tables and confirm fact table foreign keys point to the five dimensions. The schema is a teaching model; add provider-specific billing columns as required.
