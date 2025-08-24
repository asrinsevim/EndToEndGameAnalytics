-----

# End-to-End Game Analytics Data Pipeline

-----

## 🚀 Project Summary

This project is a complete, end-to-end simulation of a data analytics pipeline for a mobile game. It was designed to tackle the real-world challenge of transforming raw, nested player event data into actionable business insights. The pipeline ingests data, processes it in a cloud data warehouse, and presents the final Key Performance Indicators (KPIs) in an interactive dashboard, empowering stakeholders like product managers and marketers to make data-informed decisions.

-----

## 📊 Live KPI Dashboard

An interactive dashboard was created in Looker Studio to visualize the final, aggregated data.

**[➡️ View the Live Interactive Dashboard](https://lookerstudio.google.com/reporting/ae73a8d5-1339-4f59-ae5c-20e12e18e71a)**

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


