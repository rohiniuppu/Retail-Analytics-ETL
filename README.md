# Retail Sales Data Engineering Pipeline

This project provides a starter retail analytics pipeline that:
- ingests CSV sales data from data/raw
- cleans and transforms the data
- writes warehouse-ready output files to data/warehouse
- includes tests and a script entry point

## Quick start

1. Install dependencies:
   `py -3 -m pip install -r requirements.txt`
2. Run the pipeline:
   `py -3 scripts/run_pipeline.py`
3. Run tests:
   `py -3 -m pytest -q`

## Project structure

- src/retail_pipeline/etl.py: ETL logic
- scripts/run_pipeline.py: batch execution entry point
- tests/test_pipeline.py: regression tests
- data/raw: sample raw CSVs
- data/warehouse: cleaned output files
