# End-to-End Game Analytics Data Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Google BigQuery](https://img.shields.io/badge/Google_BigQuery-4285F4?style=for-the-badge&logo=google-bigquery&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=sql&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker_Studio-4285F4?style=for-the-badge&logo=google-data-studio&logoColor=white)

---

## 🚀 Project Summary

This project demonstrates an end-to-end data pipeline that processes live event data for a mobile game. It showcases a complete workflow from data collection in **Firebase** to transformation in **BigQuery** and final visualization in a **Looker Studio** dashboard, providing actionable insights for business stakeholders such as product managers and marketing teams.

---

## 📊 Live KPI Dashboard

An interactive dashboard was created in Looker Studio to provide a high-level overview of the game's daily performance.

**[➡️ View the Live Interactive Dashboard](https://lookerstudio.google.com/reporting/ae73a8d5-1339-4f59-ae5c-20e12e18e71a)**

---

## 🛠️ Technical Architecture

The data flows through a modern, cloud-based analytics architecture:

1.  **Data Collection:** A Python script simulates player activity and sends events directly to a live Firebase project using the **Google Analytics Measurement Protocol**.
2.  **Automated Data Export:** The native **Firebase-to-BigQuery integration** is enabled, which automatically exports raw, nested event data to BigQuery tables on a daily basis.
3.  **Data Warehousing:** **Google BigQuery** is used as a scalable, high-performance cloud data warehouse to store the raw event logs.
4.  **Data Transformation:** An advanced **SQL query** runs in BigQuery to transform the raw, nested JSON data into a clean, aggregated `daily_kpi_summary` table.
5.  **Data Visualization:** The final KPI table in BigQuery is connected to **Looker Studio** to build the interactive business intelligence dashboard.

---

## ✨ Key Technical Features

* **Live Data Ingestion:** Utilized Python and the Google Analytics Measurement Protocol to send event data to a live Firebase project.
* **Automated Cloud ETL:** Leveraged the native Firebase-to-BigQuery integration to automate the daily export of raw data.
* **Advanced SQL Transformation:** Wrote a multi-CTE (Common Table Expression) SQL query to handle a complex, real-world data problem.
    * **Parsed Nested JSON:** Successfully parsed and extracted values from the nested `event_params` schema native to Firebase exports.
    * **Data Flattening:** Used `CROSS JOIN UNNEST` to transform granular event data into an analyzable format.
* **Interactive BI Dashboard:** Created a professional dashboard in Looker Studio from scratch, featuring high-level KPI scorecards, time-series charts, and interactive date range filters.

---

## 📈 Core KPIs Analyzed

The final dashboard and summary table track the following core business metrics:
* Daily Active Users (DAU)
* Total Daily Revenue
* Average Revenue Per User (ARPU)
* Total Session Starts
* Total Purchase Events
* Total Levels Completed

---
