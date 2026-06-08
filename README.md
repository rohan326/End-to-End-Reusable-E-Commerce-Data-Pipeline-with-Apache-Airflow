# End-to-End-Reusable-E-Commerce-Data-Pipeline-with-Apache-Airflow

## Overview
This project demonstrates a production-style ETL (Extract, Transform, Load) pipeline that automates the ingestion of e-commerce data from a REST API, performs data cleansing and transformation using Python and Pandas, loads curated datasets into MySQL, and orchestrates the workflow using Apache Airflow.

The pipeline is designed to be reusable, scalable, and modular, allowing additional APIs and datasets to be integrated with minimal code changes.
## Architecture

![Architecture Diagram](docs/architecture.png)

## Business Problem

Organizations rely on data from multiple operational systems to support analytics and reporting. Manual extraction and preparation of data is time-consuming, error-prone, and difficult to scale.

This project addresses that challenge by building an automated ETL framework that:

* Extracts e-commerce data from external APIs
* Standardizes and validates incoming records
* Loads clean data into a centralized database
* Automates execution through workflow orchestration
* Provides analytics-ready datasets for reporting

## Data Source

**DummyJSON E-Commerce API**

Datasets Ingested:

* Products
* Users
* Shopping Carts

API Endpoint:

```text
https://dummyjson.com
```

---

## Technology Stack

| Component              | Technology          |
| ---------------------- | ------------------- |
| Programming Language   | Python              |
| Data Processing        | Pandas              |
| API Integration        | Requests            |
| Database               | MySQL               |
| Database Connector     | SQLAlchemy, PyMySQL |
| Workflow Orchestration | Apache Airflow      |
| Data Visualization     | Power BI            |
| Version Control        | Git & GitHub        |

## Project Structure

```text
ecommerce-etl-airflow/

├── docs/
│   └── architecture.png

├── sql/
│   └── ecommerce_database.sql

├── Extract.py
├── Transform.py
├── Load.py
├── Main.py

├── requirements.txt
├── README.md
└── .gitignore
```

## ETL Workflow

### 1. Extract

Data is retrieved from the DummyJSON API using Python requests.

Features:

* API connectivity
* Error handling
* Configurable extraction limits
* JSON response validation

### 2. Transform

Raw API responses are processed using Pandas.

Transformations include:

* Null value handling
* Column standardization
* Data type conversion
* Duplicate removal
* Data quality validation

### 3. Load

Transformed datasets are loaded into MySQL staging tables.

Tables:
* stg_products
* stg_users
* stg_carts

Features:
* Batch loading
* Transaction management
* Database validation

### 4. Orchestration
Apache Airflow automates pipeline execution.

Capabilities:

* DAG scheduling
* Workflow monitoring
* Retry mechanisms
* Logging and execution tracking
---
## Key Features
* End-to-end automated ETL pipeline
* Modular and reusable architecture
* API-driven data ingestion
* MySQL data storage
* Apache Airflow orchestration
* Logging and monitoring support
* Analytics-ready datasets
* Extensible framework for future APIs
---
## Future Enhancements

* Incremental data loading
* Star schema implementation
* Fact and dimension tables
* Data quality framework
* Docker containerization
* AWS deployment
* CI/CD automation
* Real-time data ingestion
---

## Learning Outcomes
This project demonstrates practical experience in:

* Data Engineering
* ETL Development
* API Integration
* Workflow Orchestration
* SQL and Database Design
* Data Modeling
* Data Quality Validation
* Pipeline Automation
* Analytics Engineering
---
## Author
Rohan Chandran
Data Analytics Engineer

