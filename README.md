## TL;DR
# Manufacturing Production Pipeline

## Overview
This project collects, validates, and prepares manufacturing machine data to support production analytics

## Pipeline Architecture
The data pipeline follows this flow:

1. **CSV files**  
   Raw manufacturing data exported from machines.

2. **Python processing**  
   Data cleaning, validation, and OEE calculations.

3. **SQLite database**  
   Structured storage for processed manufacturing data.

4. **Power BI dashboards**  
   Visualization of production performance and OEE metrics.
## Tech Stack

- **Python** – Data processing and OEE calculations
- **Pandas** – Data cleaning and transformation
- **SQLite** – Lightweight database for storing processed data
- **Power BI** – Data visualization and dashboards
- **CSV** – Raw manufacturing data source

## Project Structure
```text
manufacturing-data/
│
├── data
│   ├── raw
│   │   └── production_data.csv
│   │
│   └── processed
│       ├── production_clean.csv
│       └── machine_summary.csv
│
├── ingestion
│   └── ingest.py
│
├── transformation
│   └── transform.py
│
├── warehouse
│   ├── load.py
│   ├── queries.py
│   └── manufacturing.db
│
├── reporting
│   └── export.py
│
├── .gitignore
└── README.md
```
## Project Structure

- **data/raw**  
  Raw manufacturing data exported from machines.

- **data/processed**  
  Cleaned datasets generated during the transformation step.

- **ingestion**  
  Scripts responsible for loading raw CSV data.

- **transformation**  
  Data cleaning and OEE calculations.

- **warehouse**  
  Storage logic and SQL queries for the SQLite database.

- **reporting**  
  Data exports used for dashboards and analysis.
## How to Run

Follow these steps to execute the data pipeline.

### 1. Clone the repository

git clone https://github.com/your-username/manufacturing-data.git  
cd manufacturing-data

### 2. Install dependencies

Make sure Python 3.9+ is installed.

pip install pandas

### 3. Run data ingestion

Load raw manufacturing data from the CSV source.

python ingestion/ingest.py

### 4. Run data transformation

Clean the data and calculate production metrics such as OEE.

python transformation/transform.py

### 5. Load data into the warehouse

Store the processed data in the SQLite database.

python warehouse/load.py

### 6. Generate reporting data

Export processed datasets used for dashboards.

python reporting/export.py

### 7. Connect Power BI

Open Power BI and connect to the SQLite database or the processed CSV files to build dashboards.