# Microsoft Fabric Data Engineering Project

This repository contains a data engineering project implemented on Microsoft Fabric platform, showcasing various data processing and analytics capabilities.

## Project Structure

```
├── Dashboard/         # Power BI dashboards and reports
├── eventhouse/        # Event House for real-time analytics
├── eventstream/       # Event Stream processing
├── images/           # Architecture diagrams and documentation images
├── lakehouse/        # OneLake storage and processing
├── notebook/         # Data engineering notebooks
└── pipeline/         # Data pipeline definitions
```

## Components

### Lakehouse
- Centralized data storage using OneLake
- Delta Lake format for efficient data processing
- Data organization in bronze, silver, and gold layers

### Event Stream
- Real-time data ingestion
- Stream processing capabilities
- Event-driven architecture components

### Event House
- Real-time analytics processing
- Time-series data handling
- Event correlation and analysis

### Notebooks
- Data transformation scripts
- Data quality checks
- ETL processes

### Pipelines
- Data orchestration workflows
- Scheduled data processing
- Data movement and transformation

### Dashboards
- Power BI visualizations
- Business intelligence reports
- Data insights and analytics

## Getting Started

1. Ensure you have access to Microsoft Fabric workspace
2. Clone this repository
3. Set up necessary permissions and connections
4. Review and modify pipeline configurations as needed
5. Run initial data processing jobs

## Architecture

The project follows a modern data architecture pattern:
- Data ingestion through Event Stream for weather data from Weather Stack API. (for streaming data).
- Using COPY activity in Pipeline to pull data from treasury API. (for batch data).
- Processing and transformation using Notebooks.
- Storage treasury data in Lakehouse.
- Storage weather data in KQL Database.
- Visualization through Power BI Dashboards.

***Notes: I will provide HLD Diagram later.***

## Linage View for Data Flow

### Treasury Data
![Treasury Data Lineage View](images/Linage%20View%20Treasury%20Data.png)

### Weather Data
![Weather Data Lineage View](images/Linage%20View%20Weather%20Data.png)

## License

This project is licensed under the MIT License - see the LICENSE file for details.