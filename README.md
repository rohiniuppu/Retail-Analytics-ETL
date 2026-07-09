# Retail Sales Data Engineering Pipeline

This project provides a starter retail analytics pipeline for sales data that:
- ingests CSV files from data/raw
- cleans and transforms the data
- writes warehouse-ready output files to data/warehouse
- includes tests and a script entry point
- supports containerized execution with Docker and Docker Compose
- includes a Kubernetes deployment example
- provides a cloud storage hook for AWS S3, Azure Blob Storage, or GCS
- includes a simple forecasting starter using scikit-learn

## Quick start

1. Install dependencies:
   `py -3 -m pip install -r requirements.txt`
2. Run the pipeline locally:
   `py -3 scripts/run_pipeline.py`
3. Run tests:
   `py -3 -m pytest -q`

## Docker

Build and run the container:

```bash
docker build -t retail-pipeline .
docker run --rm -v "${PWD}/data:/app/data" retail-pipeline
```

Or use Docker Compose:

```bash
docker-compose up
```

## Kubernetes

A basic deployment manifest is available in `k8s-deployment.yaml`.

## Cloud storage

Set `CLOUD_DESTINATION` to enable a cloud target for the processed output.

## Project structure

- src/retail_pipeline/etl.py: ETL logic
- src/retail_pipeline/cloud_loader.py: cloud storage upload hook
- src/retail_pipeline/forecasting.py: simple forecasting starter
- scripts/run_pipeline.py: batch execution entry point
- tests/test_pipeline.py: regression tests
- data/raw: sample raw CSVs
- data/warehouse: cleaned output files
- Dockerfile: container definition
- docker-compose.yml: local container orchestration
- k8s-deployment.yaml: Kubernetes deployment example
