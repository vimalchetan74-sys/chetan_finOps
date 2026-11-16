# Day 5 — Database Optimization & Indexing
Create/load `billing_usage`, capture the query plan before indexes, run the index statements, then capture it again. SQLite `EXPLAIN QUERY PLAN` reports the chosen access plan, not a complete benchmark. For actual timing, repeat queries on a larger controlled dataset and report median runtime across several runs. Discuss index storage and write overhead.
