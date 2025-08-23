-----

# End-to-End Game Analytics Data Pipeline

-----

## 🚀 Project Summary

This project is a complete, end-to-end simulation of a data analytics pipeline for a mobile game. It was designed to tackle the real-world challenge of transforming raw, nested player event data into actionable business insights. The pipeline ingests data, processes it in a cloud data warehouse, and presents the final Key Performance Indicators (KPIs) in an interactive dashboard, empowering stakeholders like product managers and marketers to make data-informed decisions.

-----

## 📊 Live KPI Dashboard

An interactive dashboard was created in Looker Studio to visualize the final, aggregated data.

**[➡️ View the Live Interactive Dashboard](https://www.google.com/search?q=https://your-looker-studio-link-here)**

> **Note:** Please replace the link above and add a screenshot of your dashboard named `dashboard_screenshot.png` to your repository.

-----

## 🛠️ Technical Architecture

The flow of data from generation to visualization is as follows:

```
[Python Script] ---> [firebase_events_export.csv] ---> [Google BigQuery]
                                                              |
                                                              | (SQL Transformation)
                                                              v
                                         [daily_kpi_summary table] ---> [Looker Studio Dashboard]
```

-----

## ✨ Key Features & Technical Highlights

  * **Cloud Data Warehousing:** Utilized Google BigQuery for scalable and efficient storage of raw analytical data.
  * **Advanced SQL Transformation:** Wrote a multi-CTE (Common Table Expression) SQL query to handle a complex, real-world data problem.
      * **Parsed Nested JSON:** Successfully parsed and extracted values from nested JSON data stored as a string within the table.
      * **Data Flattening:** Used `CROSS JOIN UNNEST` to flatten the repeated `event_params` records into a queryable format.
  * **Business Intelligence Dashboard:** Created a professional, interactive dashboard in Looker Studio from scratch, featuring:
      * High-level KPI scorecards (Total Revenue, Average DAU, etc.).
      * Time-series charts to analyze daily trends.
      * Detailed tables for granular analysis.
      * Interactive date range filters for dynamic reporting.

-----

## ⚙️ Setup & Usage

To replicate this project:

1.  **Prerequisites:**

      * Python 3.x
      * A Google Cloud Platform account with BigQuery enabled.

2.  **Configuration & Data Generation:**

      * Run the `generate_csv_for_bigquery.py` script to create the `firebase_events_export.csv` data file.
        ```bash
        python generate_csv_for_bigquery.py
        ```

3.  **Data Ingestion:**

      * In BigQuery, create a new dataset.
      * Create a new table within the dataset by uploading the `firebase_events_export.csv` file, using the "Auto-detect schema" feature.

4.  **Data Transformation:**

      * Execute the main SQL analysis query (found in `analysis_query.sql`) in BigQuery.
      * Save the results of the query as a new table named `daily_kpi_summary`.

5.  **Visualization:**

      * Connect the `daily_kpi_summary` table from BigQuery as a data source in a new Looker Studio report.


